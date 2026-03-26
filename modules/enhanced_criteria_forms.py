# Enhanced Criteria Forms with Quantitative Data Entry
import streamlit as st
import os
import re
from datetime import datetime

def create_enhanced_criteria_forms(analyzer, criterion_num, existing_responses, application_id, db):
    """Create enhanced criteria forms with quantitative data entry"""
    
    from config.naac_config import CRITERIA, METRICS
    from modules.metric_guidance import METRIC_GUIDANCE, calculate_auto_score
    
    criterion = CRITERIA[criterion_num]
    
    st.header(f"Criterion {criterion_num}: {criterion['name']}")
    st.markdown(f"**Weight:** {criterion['weight']} marks | **Description:** {criterion['description']}")
    
    # Show IPOI explanation
    with st.expander("ℹ️ About IPOI Framework", expanded=False):
        st.markdown("""
        | Dimension | Description |
        |-----------|-------------|
        | **Input** | Resources, policies, foundational elements |
        | **Process** | Implementation, methodologies, activities |
        | **Outcome** | Immediate results and achievements |
        | **Impact** | Long-term effects and societal benefits |
        """)
    
    # Get metrics for this criterion
    criterion_metrics = {k: v for k, v in METRICS.items() if k.startswith(f'{criterion_num}.')}
    
    # Group by IPO type
    ipo_groups = {"Input": [], "Process": [], "Outcome": [], "Impact": []}
    for metric_code, metric_data in criterion_metrics.items():
        ipo_groups[metric_data['ipo']].append((metric_code, metric_data))
    
    new_responses = {}
    
    # Create forms for each IPO group
    for ipo_type in ["Input", "Process", "Outcome", "Impact"]:
        if ipo_groups[ipo_type]:
            st.subheader(f"📊 {ipo_type} Metrics")
            st.caption(f"These metrics assess the {ipo_type.lower()} dimension")
            
            for metric_code, metric_data in ipo_groups[ipo_type]:
                with st.container():
                    # Get guidance if available
                    guidance = METRIC_GUIDANCE.get(metric_code, {})
                    
                    st.markdown(f"### {metric_code}: {metric_data['name']}")
                    st.markdown(f"**Weight:** {metric_data['weight']} marks | **Type:** {metric_data['ipo']}")
                    st.markdown(f"**Description:** {metric_data['description']}")
                    
                    # Show guidance if available
                    if guidance:
                        with st.expander("ℹ️ Detailed Guidance (What's needed, how to calculate)", expanded=False):
                            st.markdown(guidance.get('what_is_needed', 'No guidance available'))
                            st.markdown("**How to Calculate:**")
                            st.markdown(guidance.get('how_to_calculate', 'No calculation method provided'))
                            
                            if guidance.get('example_response'):
                                st.markdown("**Example Response:**")
                                st.info(guidance['example_response'][:500] + "...")
                    
                    # Required documents section
                    if metric_data.get('documents'):
                        st.markdown("**📎 Required Documents:**")
                        for doc in metric_data['documents']:
                            st.markdown(f"- {doc}")
                    
                    # Get existing data
                    existing = existing_responses.get(metric_code, {})
                    existing_response = existing.get('response', {}) if existing else {}
                    
                    # Check if this metric has quantitative fields
                    if guidance and guidance.get('calculation_fields'):
                        # QUANTITATIVE METRIC - Show number input fields
                        st.markdown("**📊 Quantitative Data Entry**")
                        
                        # Create input fields for each calculation field
                        quantitative_data = {}
                        for field in guidance['calculation_fields']:
                            field_value = existing_response.get(field['field'], 0) if isinstance(existing_response, dict) else 0
                            
                            if field['type'] == 'number':
                                quantitative_data[field['field']] = st.number_input(
                                    field['label'],
                                    min_value=field.get('min', 0),
                                    value=int(field_value),
                                    step=1,
                                    key=f"num_{metric_code}_{field['field']}"
                                )
                            elif field['type'] == 'checkbox':
                                quantitative_data[field['field']] = st.checkbox(
                                    field['label'],
                                    value=bool(field_value),
                                    key=f"chk_{metric_code}_{field['field']}"
                                )
                        
                        # Auto-calculate and display score
                        score, score_message = calculate_auto_score(metric_code, quantitative_data)
                        if score is not None:
                            if score >= 3.5:
                                st.success(f"**Calculated Score:** {score:.1f}/4.0 - {score_message}")
                            elif score >= 2.5:
                                st.info(f"**Calculated Score:** {score:.1f}/4.0 - {score_message}")
                            elif score >= 1.5:
                                st.warning(f"**Calculated Score:** {score:.1f}/4.0 - {score_message}")
                            else:
                                st.error(f"**Calculated Score:** {score:.1f}/4.0 - {score_message}")
                        
                        # Qualitative description field (optional)
                        st.markdown("**📝 Additional Description (Optional)**")
                        qualitative_response = st.text_area(
                            "Provide additional context or explanation:",
                            value=existing_response.get('description', '') if isinstance(existing_response, dict) else '',
                            height=100,
                            key=f"text_{metric_code}"
                        )
                        
                        # Combine quantitative and qualitative data
                        response_data = {
                            **quantitative_data,
                            'description': qualitative_response
                        }
                        
                    else:
                        # QUALITATIVE METRIC - Simple text area
                        response_data = st.text_area(
                            "Your Response:", 
                            value=existing_response if isinstance(existing_response, str) else '',
                            height=150,
                            key=f"text_{metric_code}"
                        )
                        
                        # Real-time feedback
                        if response_data and len(response_data) > 500:
                            st.success("✅ Excellent detail! This will score well.")
                        elif response_data and len(response_data) > 200:
                            st.info("👍 Good detail. Consider adding more specifics.")
                        elif response_data and len(response_data) > 50:
                            st.warning("⚠️ Response is brief. Add more details.")
                        elif response_data:
                            st.error("❌ Response too short.")
                    
                    # Document upload section with separate buttons for each document
                    if metric_data.get('documents'):
                        st.markdown("**📤 Upload Supporting Documents**")
                        
                        # Create upload directory
                        upload_dir = f"data/uploads/{application_id}/{metric_code}"
                        os.makedirs(upload_dir, exist_ok=True)
                        
                        # Get existing documents
                        existing_docs = existing.get('documents', []) if existing else []
                        
                        # Track uploaded documents
                        uploaded_docs = {}
                        
                        # Separate upload button for each required document
                        for doc_name in metric_data['documents']:
                            # Check if already uploaded
                            doc_uploaded = False
                            for existing_doc in existing_docs:
                                if doc_name.lower() in existing_doc.lower():
                                    doc_uploaded = True
                                    uploaded_docs[doc_name] = existing_doc
                                    st.info(f"✅ {doc_name}: {existing_doc}")
                                    break
                            
                            if not doc_uploaded:
                                uploaded_file = st.file_uploader(
                                    f"📄 {doc_name}",
                                    type=['pdf', 'docx', 'xlsx', 'xls', 'jpg', 'png', 'jpeg'],
                                    key=f"upload_{metric_code}_{doc_name.replace(' ', '_')}",
                                    label_visibility="visible"
                                )
                                
                                if uploaded_file:
                                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                                    safe_filename = f"{doc_name}_{timestamp}_{uploaded_file.name}"
                                    file_path = os.path.join(upload_dir, safe_filename)
                                    
                                    with open(file_path, "wb") as f:
                                        f.write(uploaded_file.getbuffer())
                                    
                                    uploaded_docs[doc_name] = safe_filename
                                    st.success(f"✅ {doc_name} uploaded!")
                        
                        # Collect all document names
                        all_documents = list(uploaded_docs.values()) if uploaded_docs else existing_docs
                        
                    else:
                        all_documents = existing.get('documents', []) if existing else []
                    
                    # Store response
                    new_responses[metric_code] = {
                        'response': response_data,
                        'documents': all_documents
                    }
                    
                    st.markdown("---")
    
    return new_responses

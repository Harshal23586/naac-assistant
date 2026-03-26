import streamlit as st
import sys
import os
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.naac.criteria_forms import create_criteria_forms
from modules.naac.scoring_engine import NAACScoringEngine
from modules.naac.gap_analysis import create_gap_analysis
from modules.naac.report_generator import generate_ssr
from config.naac_config import CRITERION_WEIGHTAGES

st.set_page_config(page_title="NAAC Accreditation Assistant", layout="wide")

st.title("🏛️ NAAC Accreditation Assistant")

st.markdown("""
<div style='background: linear-gradient(135deg, #1e3a5f 0%, #0a2a44 100%); 
            padding: 20px; border-radius: 12px; margin-bottom: 20px;'>
    <h3 style='color: white; margin: 0;'>🎯 Welcome to NAAC Accreditation Assistant</h3>
    <p style='color: #e0e0e0; margin: 10px 0 0 0;'>
        This comprehensive tool helps you prepare for NAAC accreditation by guiding you through all 7 criteria,
        calculating your estimated CGPA, identifying gaps, and generating a draft Self-Study Report.
    </p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'naac_responses' not in st.session_state:
    st.session_state.naac_responses = {}
if 'naac_institution_name' not in st.session_state:
    st.session_state.naac_institution_name = "Your Institution"

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["📝 Data Entry", "📊 Gap Analysis", "📄 Score Report", "📑 SSR Generator"])

# Tab 1: Data Entry
with tab1:
    st.header("📝 NAAC Data Entry")
    st.markdown("Enter data for each criterion as per NAAC requirements")
    
    criterion = st.selectbox(
        "Select Criterion to work on:",
        [
            "Criterion 1: Curricular Aspects (150 marks)",
            "Criterion 2: Teaching-Learning and Evaluation (200 marks)",
            "Criterion 3: Research, Innovations and Extension (250 marks)",
            "Criterion 4: Infrastructure and Learning Resources (100 marks)",
            "Criterion 5: Student Support and Progression (100 marks)",
            "Criterion 6: Governance, Leadership and Management (100 marks)",
            "Criterion 7: Institutional Values and Best Practices (100 marks)"
        ]
    )
    
    # FIXED: Extract criterion number using regex
    import re
    match = re.search(r'Criterion (\d+)', criterion)
    if match:
        criterion_num = int(match.group(1))
    else:
        criterion_num = 1
    
    # Create form for selected criterion
    new_responses = create_criteria_forms(None, criterion_num, st.session_state.naac_responses)
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("💾 Save Criterion", type="primary"):
            st.session_state.naac_responses.update(new_responses)
            st.success(f"✅ {criterion} data saved successfully!")
    
    # Show progress
    st.markdown("---")
    st.subheader("📊 Overall Progress")
    
    completed = sum(1 for r in st.session_state.naac_responses.values() if r.get('response'))
    total = 78
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Completed Metrics", f"{completed}/{total}")
    with col2:
        st.metric("Completion Rate", f"{(completed/total*100):.1f}%")
    with col3:
        st.metric("Remaining", f"{total - completed}")
    
    st.progress(completed/total if total > 0 else 0)

# Tab 2: Gap Analysis
with tab2:
    create_gap_analysis(None, {'metric_responses': st.session_state.naac_responses})

# Tab 3: Score Report
with tab3:
    scoring_engine = NAACScoringEngine()
    cgpa = scoring_engine.calculate_cgpa(st.session_state.naac_responses)
    grade = scoring_engine.get_grade(cgpa)
    criterion_scores = scoring_engine.calculate_criterion_score(st.session_state.naac_responses)
    
    st.header("🎯 NAAC Score Report")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Estimated CGPA", f"{cgpa:.2f}/4.00", delta=f"Target: 3.26")
    with col2:
        st.metric("Projected Grade", grade, delta="A+ target")
    with col3:
        total_score = cgpa * 250
        st.metric("Total Score", f"{total_score:.0f}/1000")
    with col4:
        completed = sum(1 for r in st.session_state.naac_responses.values() if r.get('response'))
        total = 78
        st.metric("Completion", f"{(completed/total*100):.1f}%")
    
    st.markdown("---")
    st.subheader("📊 Criterion-wise Performance")
    
    for criterion in range(1, 8):
        score = criterion_scores.get(criterion, 0)
        weight = CRITERION_WEIGHTAGES[criterion]
        weighted_score = score * weight
        
        st.write(f"**Criterion {criterion}** (Weight: {weight} marks)")
        st.progress(score/4, text=f"Score: {score:.2f}/4.00 | Weighted: {weighted_score:.0f}/{weight}")
    
    st.markdown("---")
    st.subheader("💡 Recommendations")
    
    if cgpa < 2.0:
        st.error("⚠️ **Critical:** Your estimated CGPA is below B grade. Immediate action required!")
        st.write("Focus on completing all metrics and verifying data accuracy.")
    elif cgpa < 3.0:
        st.warning("📊 **Improvement Needed:** Focus on completing missing metrics.")
        weak_criteria = [c for c in range(1, 8) if criterion_scores.get(c, 0) < 2.5]
        if weak_criteria:
            st.write(f"**Priority Areas:** {', '.join([f'Criterion {c}' for c in weak_criteria])}")
    else:
        st.success("✅ **Great Progress!** Continue completing remaining metrics.")
        st.write("**Next Steps:** Complete all metrics, prepare supporting documents, and generate SSR.")

# Tab 4: SSR Generator
with tab4:
    generate_ssr(None, {
        'metric_responses': st.session_state.naac_responses,
        'institution_name': st.session_state.naac_institution_name,
        'cycle': 1
    })

# Sidebar information
st.sidebar.markdown("---")
st.sidebar.subheader("📋 NAAC Information")
st.sidebar.info("""
**Total Weightage:** 1000 marks

**Grade Thresholds:**
- A++: 3.51 - 4.00
- A+: 3.26 - 3.50
- A: 3.01 - 3.25
- B++: 2.76 - 3.00
- B+: 2.51 - 2.75
- B: 2.01 - 2.50
- C: 1.51 - 2.00
- D: ≤ 1.50
""")

completed = sum(1 for r in st.session_state.naac_responses.values() if r.get('response'))
total = 78
st.sidebar.progress(completed/total if total > 0 else 0)
st.sidebar.caption(f"Progress: {completed}/{total} metrics")

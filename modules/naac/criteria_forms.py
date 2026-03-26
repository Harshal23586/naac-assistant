# All 10 Criteria Forms with IPOI Framework
import streamlit as st
import pandas as pd
from datetime import datetime
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.naac_config import CRITERIA, METRICS

def create_criteria_forms(analyzer, criterion_num, responses):
    """Create form for a specific criterion with IPOI sections"""
    criterion = CRITERIA[criterion_num]
    
    st.header(f"Criterion {criterion_num}: {criterion['name']}")
    st.markdown(f"**Weight:** {criterion['weight']} marks")
    st.markdown(f"**Description:** {criterion['description']}")
    st.markdown(f"**Assessment Dimensions:** {' → '.join(criterion['ipo_indicators'])}")
    st.markdown("---")
    
    # Get metrics for this criterion
    criterion_metrics = {k: v for k, v in METRICS.items() 
                        if k.startswith(f'{criterion_num}.')}
    
    # Group by IPOI type
    ipo_groups = {"Input": [], "Process": [], "Outcome": [], "Impact": []}
    for metric_code, metric_data in criterion_metrics.items():
        ipo_groups[metric_data['ipo']].append((metric_code, metric_data))
    
    # Display forms by IPOI section
    new_responses = {}
    
    for ipo_type in ["Input", "Process", "Outcome", "Impact"]:
        if ipo_groups[ipo_type]:
            st.subheader(f"📊 {ipo_type} Metrics")
            st.caption(f"These metrics assess the {ipo_type.lower()} dimension of {criterion['name']}")
            
            for metric_code, metric_data in ipo_groups[ipo_type]:
                new_responses.update(
                    create_metric_form(metric_code, metric_data, responses.get(metric_code, {}))
                )
    
    return new_responses

def create_metric_form(metric_code, metric_data, existing_response):
    """Create form for a single metric"""
    st.markdown(f"**{metric_code}: {metric_data['name']}**")
    st.caption(f"Weight: {metric_data['weight']} marks | Type: {metric_data['ipo']}")
    st.caption(f"Description: {metric_data['description']}")
    
    # Required documents display
    if metric_data.get('documents'):
        st.markdown("**Required Documents:**")
        for doc in metric_data['documents']:
            st.markdown(f"- 📄 {doc}")
    
    # Form based on IPO type
    if metric_data['ipo'] == "Input":
        response = create_input_form(metric_code, metric_data, existing_response.get('response'))
    elif metric_data['ipo'] == "Process":
        response = create_process_form(metric_code, metric_data, existing_response.get('response'))
    elif metric_data['ipo'] == "Outcome":
        response = create_outcome_form(metric_code, metric_data, existing_response.get('response'))
    else:  # Impact
        response = create_impact_form(metric_code, metric_data, existing_response.get('response'))
    
    st.markdown("---")
    return {metric_code: {'response': response, 'documents': []}}

def create_input_form(metric_code, metric_data, existing):
    """Create form for Input metrics"""
    col1, col2 = st.columns(2)
    
    with col1:
        if "Curriculum" in metric_data['name']:
            response = st.text_area("Describe curriculum content and structure:", 
                                    value=existing.get('description', '') if existing else '',
                                    height=150)
            url = st.text_input("URL where content is publicly available:", 
                               value=existing.get('url', '') if existing else '')
            return {'description': response, 'url': url}
        
        elif "Faculty" in metric_data['name']:
            count = st.number_input("Number of applications received:", 
                                   value=existing.get('applications', 0) if existing else 0)
            return {'applications': count}
        
        elif "Research" in metric_data['name']:
            has_policy = st.checkbox("Has research policy?", 
                                    value=existing.get('has_policy', False) if existing else False)
            return {'has_policy': has_policy}
        
        elif "Financial" in metric_data['name']:
            budget = st.number_input("Budget allocation (INR in Lakhs):", 
                                    value=existing.get('budget', 0) if existing else 0.0)
            return {'budget': budget}
        
        else:
            response = st.text_area("Describe the inputs/resources available:", 
                                   value=existing.get('description', '') if existing else '',
                                   height=100)
            return {'description': response}
    
    with col2:
        doc = st.file_uploader("Upload supporting document", 
                              key=f"doc_{metric_code}", 
                              type=['pdf', 'docx', 'xlsx'])
        if doc:
            st.success(f"✓ {doc.name} uploaded")
    
    return existing if existing else {}

def create_process_form(metric_code, metric_data, existing):
    """Create form for Process metrics"""
    col1, col2 = st.columns(2)
    
    with col1:
        if "Review" in metric_data['name'] or "Process" in metric_data['name']:
            st.markdown("**Implementation Details:**")
            frequency = st.selectbox("Review frequency:", 
                                    ["Annual", "Semi-annual", "Quarterly", "As needed"],
                                    index=["Annual", "Semi-annual", "Quarterly", "As needed"].index(existing.get('frequency', 'Annual')) if existing else 0)
            
            committee_exists = st.checkbox("Has review committee?", 
                                          value=existing.get('has_committee', False) if existing else False)
            
            stakeholder_input = st.multiselect("Stakeholders involved:", 
                                              ["Students", "Teachers", "Employers", "Alumni", "Industry"],
                                              default=existing.get('stakeholders', []) if existing else [])
            
            return {'frequency': frequency, 'has_committee': committee_exists, 'stakeholders': stakeholder_input}
        
        elif "Teaching" in metric_data['name']:
            methods = st.multiselect("Teaching methods used:", 
                                    ["Interactive", "Experiential", "Collaborative", "Problem-based", "ICT-enabled"],
                                    default=existing.get('methods', []) if existing else [])
            
            digital_tools = st.text_input("Digital tools/platforms used:", 
                                         value=existing.get('digital_tools', '') if existing else '')
            
            return {'methods': methods, 'digital_tools': digital_tools}
        
        elif "Research" in metric_data['name']:
            collaborations = st.number_input("Number of research collaborations:", 
                                            value=existing.get('collaborations', 0) if existing else 0)
            
            interdisciplinary = st.checkbox("Interdisciplinary research encouraged?", 
                                           value=existing.get('interdisciplinary', False) if existing else False)
            
            return {'collaborations': collaborations, 'interdisciplinary': interdisciplinary}
        
        else:
            description = st.text_area("Describe the process and its implementation:", 
                                      value=existing.get('description', '') if existing else '',
                                      height=150)
            return {'description': description}
    
    with col2:
        doc = st.file_uploader("Upload process documentation", 
                              key=f"doc_{metric_code}", 
                              type=['pdf', 'docx', 'xlsx'])
        if doc:
            st.success(f"✓ {doc.name} uploaded")
    
    return existing if existing else {}

def create_outcome_form(metric_code, metric_data, existing):
    """Create form for Outcome metrics"""
    col1, col2 = st.columns(2)
    
    with col1:
        if "Learning" in metric_data['name'] or "Outcomes" in metric_data['name']:
            pass_percentage = st.slider("Pass percentage:", 0, 100, 
                                       value=int(existing.get('pass_percentage', 75)) if existing else 75)
            
            completion_rate = st.slider("Course completion rate (%):", 0, 100, 
                                       value=int(existing.get('completion_rate', 85)) if existing else 85)
            
            return {'pass_percentage': pass_percentage, 'completion_rate': completion_rate}
        
        elif "Publications" in metric_data['name'] or "Patents" in metric_data['name']:
            publications = st.number_input("Number of publications:", 
                                          value=existing.get('publications', 0) if existing else 0)
            
            patents = st.number_input("Number of patents:", 
                                     value=existing.get('patents', 0) if existing else 0)
            
            return {'publications': publications, 'patents': patents}
        
        elif "Placement" in metric_data['name'] or "Employment" in metric_data['name']:
            placement_rate = st.slider("Placement rate (%):", 0, 100, 
                                      value=int(existing.get('placement_rate', 70)) if existing else 70)
            
            avg_salary = st.number_input("Average salary (INR in Lakhs):", 
                                        value=existing.get('avg_salary', 0) if existing else 0.0)
            
            return {'placement_rate': placement_rate, 'avg_salary': avg_salary}
        
        else:
            achievement = st.text_area("Describe outcomes achieved:", 
                                      value=existing.get('achievement', '') if existing else '',
                                      height=100)
            
            metrics = st.text_input("Quantifiable metrics achieved:", 
                                   value=existing.get('metrics', '') if existing else '')
            
            return {'achievement': achievement, 'metrics': metrics}
    
    with col2:
        doc = st.file_uploader("Upload evidence of outcomes", 
                              key=f"doc_{metric_code}", 
                              type=['pdf', 'docx', 'xlsx'])
        if doc:
            st.success(f"✓ {doc.name} uploaded")
    
    return existing if existing else {}

def create_impact_form(metric_code, metric_data, existing):
    """Create form for Impact metrics"""
    col1, col2 = st.columns(2)
    
    with col1:
        if "Progression" in metric_data['name'] or "Success" in metric_data['name']:
            higher_edu = st.slider("Progression to higher education (%):", 0, 100, 
                                  value=int(existing.get('higher_education', 40)) if existing else 40)
            
            alumni_success = st.text_area("Alumni success stories:", 
                                         value=existing.get('alumni_stories', '') if existing else '',
                                         height=100)
            
            return {'higher_education': higher_edu, 'alumni_stories': alumni_success}
        
        elif "Citations" in metric_data['name']:
            citations = st.number_input("Total citations:", 
                                       value=existing.get('citations', 0) if existing else 0)
            
            h_index = st.number_input("h-index:", 
                                     value=existing.get('h_index', 0) if existing else 0)
            
            return {'citations': citations, 'h_index': h_index}
        
        elif "Satisfaction" in metric_data['name']:
            student_satisfaction = st.slider("Student satisfaction (%):", 0, 100, 
                                            value=int(existing.get('student_satisfaction', 75)) if existing else 75)
            
            faculty_satisfaction = st.slider("Faculty satisfaction (%):", 0, 100, 
                                            value=int(existing.get('faculty_satisfaction', 80)) if existing else 80)
            
            return {'student_satisfaction': student_satisfaction, 'faculty_satisfaction': faculty_satisfaction}
        
        else:
            impact_description = st.text_area("Describe the impact of this area:", 
                                             value=existing.get('description', '') if existing else '',
                                             height=150)
            
            evidence = st.text_input("Evidence of impact (with links):", 
                                    value=existing.get('evidence', '') if existing else '')
            
            return {'description': impact_description, 'evidence': evidence}
    
    with col2:
        doc = st.file_uploader("Upload impact evidence", 
                              key=f"doc_{metric_code}", 
                              type=['pdf', 'docx', 'xlsx'])
        if doc:
            st.success(f"✓ {doc.name} uploaded")
    
    return existing if existing else {}

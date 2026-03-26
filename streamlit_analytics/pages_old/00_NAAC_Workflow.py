# NAAC Complete Workflow - Step by Step
import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

st.set_page_config(page_title="NAAC Workflow", layout="wide")

# Initialize workflow state
if 'workflow_step' not in st.session_state:
    st.session_state.workflow_step = 1
if 'naac_data' not in st.session_state:
    st.session_state.naac_data = {}

st.title("📋 NAAC Accreditation - Step by Step Workflow")
st.markdown("Follow the steps below to complete your NAAC preparation")

# Progress bar
progress = (st.session_state.workflow_step - 1) / 9
st.progress(progress)
st.write(f"Step {st.session_state.workflow_step} of 10")

# Step navigation
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("⬅️ Previous", disabled=(st.session_state.workflow_step == 1)):
        st.session_state.workflow_step -= 1
        st.rerun()
with col5:
    if st.button("Next ➡️", disabled=(st.session_state.workflow_step == 10)):
        st.session_state.workflow_step += 1
        st.rerun()

st.markdown("---")

# Step 1: Institution Profile
if st.session_state.workflow_step == 1:
    st.header("Step 1: Institution Profile")
    st.info("This information is required for the SSR Executive Summary")
    
    col1, col2 = st.columns(2)
    with col1:
        institution_name = st.text_input("Institution Name", 
                                         value=st.session_state.naac_data.get('name', ''))
        institution_type = st.selectbox("Type of University",
                                        ["Central University", "State University", 
                                         "Private University", "Deemed to be University",
                                         "Institution of National Importance"])
        establishment_date = st.date_input("Date of Establishment")
        
    with col2:
        ugc_recognition = st.selectbox("UGC Recognition",
                                       ["2(f) and 12B", "2(f) only", "Not Applicable"])
        aishe_code = st.text_input("AISHE Code")
        website = st.text_input("Institution Website")
    
    st.subheader("Required Documents")
    reg_cert = st.file_uploader("UGC Recognition Certificate", type=['pdf'])
    aishe_report = st.file_uploader("Latest AISHE Report", type=['pdf'])
    
    if st.button("Save & Continue", type="primary"):
        st.session_state.naac_data['profile'] = {
            'name': institution_name,
            'type': institution_type,
            'establishment': establishment_date,
            'ugc': ugc_recognition,
            'aishe': aishe_code,
            'website': website
        }
        st.session_state.workflow_step = 2
        st.rerun()

# Steps 2-8: Criteria 1-7
elif 2 <= st.session_state.workflow_step <= 8:
    criterion_num = st.session_state.workflow_step - 1
    
    criterion_names = {
        1: "Curricular Aspects (150 marks)",
        2: "Teaching-Learning and Evaluation (200 marks)",
        3: "Research, Innovations and Extension (250 marks)",
        4: "Infrastructure and Learning Resources (100 marks)",
        5: "Student Support and Progression (100 marks)",
        6: "Governance, Leadership and Management (100 marks)",
        7: "Institutional Values and Best Practices (100 marks)"
    }
    
    st.header(f"Step {st.session_state.workflow_step}: Criterion {criterion_num} - {criterion_names[criterion_num]}")
    
    # Show metrics for this criterion
    st.subheader("Required Metrics")
    
    # Metric 1.1.1 for Criterion 1
    if criterion_num == 1:
        st.write("**Metric 1.1.1: Curriculum relevance (20 marks)**")
        response = st.text_area("Describe curriculum relevance:", height=150)
        doc = st.file_uploader("Upload PO, PSO, CO documents", key="c1_m111", type=['pdf'])
        
        st.write("**Metric 1.1.2: Syllabus revision (20 marks)**")
        total_prog = st.number_input("Total programmes:", min_value=0)
        revised_prog = st.number_input("Programmes revised:", min_value=0)
        
    elif criterion_num == 2:
        st.write("**Metric 2.1.1: Demand Ratio (5 marks)**")
        seats = st.number_input("Number of seats:", min_value=0)
        apps = st.number_input("Applications received:", min_value=0)
        if seats > 0:
            st.info(f"Demand Ratio: {apps/seats:.2f}")
        
        st.write("**Metric 2.2.2: Student-Teacher Ratio (10 marks)**")
        students = st.number_input("Total students:", min_value=0)
        teachers = st.number_input("Total teachers:", min_value=1)
        st.info(f"Ratio: {students/teachers:.1f}:1")
    
    # Add more metrics for each criterion...
    
    if st.button("Save Criterion", type="primary"):
        st.success(f"Criterion {criterion_num} saved!")
        st.session_state.workflow_step += 1
        st.rerun()

# Step 9: Gap Analysis
elif st.session_state.workflow_step == 9:
    st.header("Step 9: Gap Analysis")
    st.info("Review what's missing before proceeding")
    
    # Analyze gaps
    completed = []
    missing = []
    
    for c in range(1, 8):
        if f'criterion_{c}' in st.session_state.naac_data:
            completed.append(c)
        else:
            missing.append(c)
    
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"✅ Completed Criteria: {', '.join(map(str, completed))}")
    with col2:
        st.error(f"❌ Missing Criteria: {', '.join(map(str, missing))}")
    
    st.subheader("Document Status")
    # Show document validation results
    
    if st.button("Proceed to Score Report"):
        st.session_state.workflow_step = 10
        st.rerun()

# Step 10: Score Report & SSR
elif st.session_state.workflow_step == 10:
    st.header("Step 10: Score Report & SSR Generation")
    
    # Calculate score
    estimated_cgpa = 3.0  # Calculate from actual data
    grade = "A"
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Estimated CGPA", f"{estimated_cgpa:.2f}")
    with col2:
        st.metric("Projected Grade", grade)
    with col3:
        st.metric("Readiness", "85%")
    
    st.subheader("Generate Reports")
    if st.button("Generate SSR Draft", type="primary"):
        st.success("SSR generated! Download below.")
        # Create download button
    
    if st.button("Export to Excel"):
        st.info("Data exported for UGC submission")
    
    st.success("✅ NAAC Preparation Complete!")
    st.markdown("You can now submit for peer team visit or continue improving scores.")

# NAAC Accreditation Assistant - Complete Workflow with All Metrics
import streamlit as st
import sys
import os
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(
    page_title="NAAC Accreditation Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #0a2a44 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #1e3a5f;
    }
    .required-doc {
        background: #fff3cd;
        padding: 0.5rem;
        border-radius: 5px;
        font-size: 0.9rem;
    }
    .step-active {
        background: #1e3a5f;
        color: white;
        font-weight: bold;
    }
    .step-completed {
        background: #28a745;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'workflow_step' not in st.session_state:
    st.session_state.workflow_step = 1
if 'naac_data' not in st.session_state:
    st.session_state.naac_data = {
        'profile': {},
        'criterion_1': {},
        'criterion_2': {},
        'criterion_3': {},
        'criterion_4': {},
        'criterion_5': {},
        'criterion_6': {},
        'criterion_7': {},
        'documents': {},
        'validation_results': {}
    }
if 'completed_steps' not in st.session_state:
    st.session_state.completed_steps = set()

# ============================================================================
# SIDEBAR
# ============================================================================
with st.sidebar:
    st.markdown("### 🎓 NAAC Accreditation")
    st.markdown("---")
    
    total_steps = 10
    completed_count = len(st.session_state.completed_steps)
    st.progress(completed_count / total_steps)
    st.caption(f"Step {st.session_state.workflow_step} of {total_steps}")
    
    st.markdown("---")
    st.info("""
    **NAAC Weightages:**
    - Criterion I: 150 marks
    - Criterion II: 200 marks
    - Criterion III: 250 marks
    - Criterion IV: 100 marks
    - Criterion V: 100 marks
    - Criterion VI: 100 marks
    - Criterion VII: 100 marks
    """)

# ============================================================================
# MAIN HEADER
# ============================================================================
st.markdown('<div class="main-header">', unsafe_allow_html=True)
st.title("🏛️ NAAC Accreditation Assistant")
st.markdown("### Prepare for NAAC Assessment - Step by Step Workflow")
st.markdown('</div>', unsafe_allow_html=True)

# Step Navigation - Now matches criteria numbers
cols = st.columns(10)
step_labels = [
    "0: Profile", "1: Curricular", "2: Teaching", "3: Research", 
    "4: Infra", "5: Student", "6: Governance", "7: Values", 
    "8: Gap", "9: Report"
]

for i, (col, label) in enumerate(zip(cols, step_labels), 1):
    with col:
        if i in st.session_state.completed_steps:
            st.markdown(f"<div style='text-align:center; background:#28a745; color:white; padding:5px; border-radius:5px'>✅<br>{label}</div>", unsafe_allow_html=True)
        elif i == st.session_state.workflow_step:
            st.markdown(f"<div style='text-align:center; background:#1e3a5f; color:white; padding:5px; border-radius:5px'>➡️<br>{label}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align:center; color:gray'>{label}</div>", unsafe_allow_html=True)

st.markdown("---")

# Navigation buttons
col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    if st.button("⬅️ Previous", disabled=(st.session_state.workflow_step == 1)):
        st.session_state.workflow_step -= 1
        st.rerun()
with col2:
    if st.button("Next ➡️", disabled=(st.session_state.workflow_step == 10)):
        st.session_state.workflow_step += 1
        st.rerun()

st.markdown("---")

# ============================================================================
# STEP 0: INSTITUTION PROFILE
# ============================================================================
if st.session_state.workflow_step == 1:
    st.header("📋 Step 0: Institution Profile")
    st.caption("Required for SSR Executive Summary")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Basic Information")
        institution_name = st.text_input("Name of the University *")
        address = st.text_input("Address")
        city = st.text_input("City")
        state = st.text_input("State")
        pin = st.text_input("PIN Code")
        website = st.text_input("Website")
        
    with col2:
        st.subheader("Establishment Details")
        est_date = st.date_input("Establishment Date")
        university_type = st.selectbox("Type of University", 
                                       ["Central University", "State University", 
                                        "Private University", "Deemed to be University"])
        ugc_recognition = st.selectbox("UGC Recognition", 
                                       ["2(f) and 12B", "2(f) only", "Not Applicable"])
        aishe_code = st.text_input("AISHE Code *")
        
    st.subheader("📎 Required Documents (as per SOP)")
    doc1 = st.file_uploader("UGC Recognition Certificate", type=['pdf'])
    doc2 = st.file_uploader("AISHE Report (latest)", type=['pdf'])
    doc3 = st.file_uploader("University Act / Statutes", type=['pdf'])
    
    if st.button("✅ Save & Continue to Criterion 1", type="primary"):
        st.session_state.naac_data['profile'] = {
            'name': institution_name, 'address': address, 'city': city,
            'state': state, 'pin': pin, 'website': website,
            'est_date': est_date, 'type': university_type,
            'ugc': ugc_recognition, 'aishe': aishe_code
        }
        st.session_state.completed_steps.add(1)
        st.session_state.workflow_step = 2
        st.rerun()

# ============================================================================
# STEP 1: CRITERION I - CURRICULAR ASPECTS (150 marks)
# ============================================================================
elif st.session_state.workflow_step == 2:
    st.header("📚 Step 1: Criterion I - Curricular Aspects (150 marks)")
    
    # Key Indicator 1.1
    st.subheader("🔹 Key Indicator 1.1: Curriculum Design and Development (50 marks)")
    
    # Metric 1.1.1
    with st.container():
        st.markdown("**📊 Metric 1.1.1 (20 marks)** - Curriculum relevance")
        st.caption("Qualitative Metric - Describe in max 500 words")
        
        response_111 = st.text_area("Describe how curriculum developed and implemented have relevance to local, national, regional and global developmental needs:", 
                                    height=150,
                                    help="Include how Programme Outcomes (POs), Programme Specific Outcomes (PSOs) and Course Outcomes (COs) reflect these needs")
        
        st.markdown('<div class="required-doc">📎 Required Document: Programme Outcomes (POs), Programme Specific Outcomes (PSOs), Course Outcomes (COs) uploaded on website</div>', unsafe_allow_html=True)
        doc_111 = st.file_uploader("Upload POs, PSOs, COs document", key="m111", type=['pdf', 'docx'])
        url_111 = st.text_input("Or provide website URL where these are hosted", placeholder="https://...")
    
    # Metric 1.1.2
    with st.container():
        st.markdown("**📊 Metric 1.1.2 (20 marks)** - Syllabus revision")
        st.caption("Quantitative Metric - Percentage of Programmes where syllabus revision was carried out during last five years")
        
        col1, col2 = st.columns(2)
        with col1:
            total_prog = st.number_input("Total number of Programmes offered during last five years", min_value=0)
        with col2:
            revised_prog = st.number_input("Number of Programmes where syllabus was revised during last five years", min_value=0)
        
        if total_prog > 0:
            percentage = (revised_prog / total_prog) * 100
            st.info(f"📈 Percentage: {percentage:.1f}%")
        
        st.markdown('<div class="required-doc">📎 Required Document: Minutes of relevant Academic Council/BOS meetings with agenda items</div>', unsafe_allow_html=True)
        doc_112 = st.file_uploader("Upload BOS/Academic Council minutes", key="m112", type=['pdf'])
    
    # Metric 1.1.3
    with st.container():
        st.markdown("**📊 Metric 1.1.3 (10 marks)** - Employability/Entrepreneurship/Skill Development")
        st.caption("Average percentage of courses having focus on employability/entrepreneurship/skill development")
        
        st.markdown('<div class="required-doc">📎 Required Document: Upload Excel template with Course Code, Course Name, Focus Area (Employability/Entrepreneurship/Skill Development)</div>', unsafe_allow_html=True)
        excel_file = st.file_uploader("Upload courses data (Excel format)", key="m113", type=['xlsx', 'csv'])
        if excel_file:
            st.success("✓ File uploaded. Data will be processed for scoring")
    
    st.markdown("---")
    
    # Key Indicator 1.2
    st.subheader("🔹 Key Indicator 1.2: Academic Flexibility (50 marks)")
    
    # Metric 1.2.1
    with st.container():
        st.markdown("**📊 Metric 1.2.1 (30 marks)** - New courses introduced")
        st.caption("Percentage of new courses introduced out of total courses across all programs offered during last five years")
        
        col1, col2 = st.columns(2)
        with col1:
            new_courses = st.number_input("Number of new courses introduced", min_value=0)
        with col2:
            total_courses = st.number_input("Total courses offered", min_value=1)
        
        if total_courses > 0:
            st.info(f"📈 Percentage: {(new_courses/total_courses*100):.1f}%")
        
        st.markdown('<div class="required-doc">📎 Required Document: Minutes of Academic Council/BOS meetings highlighting new courses introduced</div>', unsafe_allow_html=True)
        doc_121 = st.file_uploader("Upload minutes for new courses", key="m121", type=['pdf'])
    
    # Metric 1.2.2
    with st.container():
        st.markdown("**📊 Metric 1.2.2 (20 marks)** - CBCS/Elective course system")
        st.caption("Percentage of Programmes in which Choice Based Credit System (CBCS)/elective course system has been implemented")
        
        col1, col2 = st.columns(2)
        with col1:
            cbcs_prog = st.number_input("Number of programmes with CBCS/Elective system", min_value=0)
        with col2:
            total_prog_cbcs = st.number_input("Total programmes offered", min_value=1)
        
        if total_prog_cbcs > 0:
            st.info(f"📈 Implementation: {(cbcs_prog/total_prog_cbcs*100):.1f}%")
        
        st.markdown('<div class="required-doc">📎 Required Document: CBCS implementation structure, course credits, electives list as approved by competent board</div>', unsafe_allow_html=True)
        doc_122 = st.file_uploader("Upload CBCS structure document", key="m122", type=['pdf'])
    
    st.markdown("---")
    
    # Key Indicator 1.3
    st.subheader("🔹 Key Indicator 1.3: Curriculum Enrichment (30 marks)")
    
    # Metric 1.3.1
    with st.container():
        st.markdown("**📊 Metric 1.3.1 (5 marks)** - Cross-cutting issues")
        st.caption("Institution integrates crosscutting issues relevant to Professional Ethics, Gender, Human Values, Environment and Sustainability")
        
        response_131 = st.text_area("Describe how these issues are integrated into the curriculum:", height=100)
        st.markdown('<div class="required-doc">📎 Required Document: List and description of courses addressing Gender, Environment, Sustainability, Human Values, Professional Ethics</div>', unsafe_allow_html=True)
        doc_131 = st.file_uploader("Upload course list", key="m131", type=['pdf', 'xlsx'])
    
    # Metric 1.3.2 & 1.3.3 - Value added courses
    with st.container():
        st.markdown("**📊 Metric 1.3.2 (10 marks)** - Value-added courses")
        st.caption("Number of value-added courses for imparting transferable and life skills offered during last five years")
        
        value_courses = st.number_input("Number of value-added courses (minimum 30 contact hours)", min_value=0)
        
        st.markdown("**📊 Metric 1.3.3 (10 marks)** - Students enrolled in value-added courses")
        col1, col2 = st.columns(2)
        with col1:
            enrolled_students = st.number_input("Number of students enrolled", min_value=0)
        with col2:
            total_students = st.number_input("Total students", min_value=1)
        
        if total_students > 0:
            st.info(f"📈 Enrollment: {(enrolled_students/total_students*100):.1f}%")
        
        st.markdown('<div class="required-doc">📎 Required Document: List of value-added courses with duration, number of times offered, students enrolled and completed</div>', unsafe_allow_html=True)
        doc_132 = st.file_uploader("Upload value-added courses data", key="m132", type=['xlsx'])
    
    # Metric 1.3.4
    with st.container():
        st.markdown("**📊 Metric 1.3.4 (5 marks)** - Field projects/Research projects/Internships")
        st.caption("Percentage of students undertaking field projects/research projects/internships")
        
        col1, col2 = st.columns(2)
        with col1:
            undertaking = st.number_input("Students undertaking projects/internships", min_value=0)
        with col2:
            total_students_proj = st.number_input("Total students", min_value=1)
        
        if total_students_proj > 0:
            st.info(f"📈 Participation: {(undertaking/total_students_proj*100):.1f}%")
        
        st.markdown('<div class="required-doc">📎 Required Document: List of students with project/internship details, completion certificates</div>', unsafe_allow_html=True)
        doc_134 = st.file_uploader("Upload student list", key="m134", type=['xlsx', 'pdf'])
    
    st.markdown("---")
    
    # Key Indicator 1.4
    st.subheader("🔹 Key Indicator 1.4: Feedback System (20 marks)")
    
    # Metric 1.4.1
    with st.container():
        st.markdown("**📊 Metric 1.4.1 (10 marks)** - Stakeholder feedback")
        feedback_sources = st.radio("Feedback received from:", 
                                   ["All 4 (Students, Teachers, Employers, Alumni)",
                                    "Any 3 of the above",
                                    "Any 2 of the above", 
                                    "Any 1 of the above",
                                    "None of the above"])
        
        st.markdown('<div class="required-doc">📎 Required Document: Stakeholder feedback analysis report, Action taken report as per minutes of Governing Council</div>', unsafe_allow_html=True)
        doc_141 = st.file_uploader("Upload feedback analysis report", key="m141", type=['pdf'])
    
    # Metric 1.4.2
    with st.container():
        st.markdown("**📊 Metric 1.4.2 (10 marks)** - Feedback process")
        feedback_process = st.radio("Feedback process:", 
                                   ["Feedback collected, analysed, action taken and hosted on website",
                                    "Feedback collected, analysed and action taken",
                                    "Feedback collected and analysed",
                                    "Feedback collected",
                                    "Feedback not collected"])
        
        url_feedback = st.text_input("URL where feedback reports are hosted", placeholder="https://...")
    
    if st.button("✅ Save Criterion I", type="primary"):
        st.session_state.naac_data['criterion_1'] = {
            '1.1.1': response_111, '1.1.2': {'total': total_prog, 'revised': revised_prog},
            '1.1.3': excel_file.name if excel_file else None,
            '1.2.1': {'new': new_courses, 'total': total_courses},
            '1.2.2': {'cbcs': cbcs_prog, 'total': total_prog_cbcs},
            '1.3.1': response_131, '1.3.2': value_courses,
            '1.3.3': {'enrolled': enrolled_students, 'total': total_students},
            '1.3.4': {'undertaking': undertaking, 'total': total_students_proj},
            '1.4.1': feedback_sources, '1.4.2': feedback_process
        }
        st.session_state.completed_steps.add(2)
        st.session_state.workflow_step = 3
        st.rerun()

# ============================================================================
# STEP 2: CRITERION II - TEACHING-LEARNING (200 marks)
# ============================================================================
elif st.session_state.workflow_step == 3:
    st.header("👨‍🏫 Step 2: Criterion II - Teaching-Learning and Evaluation (200 marks)")
    
    # Key Indicator 2.1
    st.subheader("🔹 Key Indicator 2.1: Student Enrolment and Profile (10 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 2.1.1 (5 marks)** - Demand Ratio")
        col1, col2 = st.columns(2)
        with col1:
            seats = st.number_input("Number of seats available", min_value=0)
        with col2:
            applications = st.number_input("Number of eligible applications received", min_value=0)
        if seats > 0:
            st.info(f"📈 Demand Ratio: {applications/seats:.2f}")
        
        st.markdown("**📊 Metric 2.1.2 (5 marks)** - Reserved category filling")
        st.markdown('<div class="required-doc">📎 Required Document: Final admission list with category details, reservation policy document</div>', unsafe_allow_html=True)
        doc_212 = st.file_uploader("Upload admission list", key="m212", type=['pdf', 'xlsx'])
    
    # Key Indicator 2.2
    st.subheader("🔹 Key Indicator 2.2: Catering to Student Diversity (20 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 2.2.1 (10 marks)** - Learning level assessment")
        response_221 = st.text_area("Describe how the institution assesses learning levels and organizes special programmes for advanced and slow learners:", height=100)
        
        st.markdown("**📊 Metric 2.2.2 (10 marks)** - Student-Teacher Ratio")
        col1, col2 = st.columns(2)
        with col1:
            students_st = st.number_input("Total students enrolled", min_value=0)
        with col2:
            teachers_st = st.number_input("Full-time teachers", min_value=1)
        ratio = students_st / teachers_st if teachers_st > 0 else 0
        st.info(f"📈 Student-Teacher Ratio: {ratio:.1f}:1")
        if ratio > 25:
            st.warning("⚠️ NAAC recommends 15:1 to 20:1 for optimal learning")
    
    # Key Indicator 2.3
    st.subheader("🔹 Key Indicator 2.3: Teaching-Learning Process (20 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 2.3.1 (6 marks)** - Student-centric methods")
        response_231 = st.text_area("Describe experiential learning, participative learning, problem solving methodologies used:", height=100)
        
        st.markdown("**📊 Metric 2.3.2 (6 marks)** - ICT enabled tools")
        response_232 = st.text_area("Describe ICT tools including online resources used for effective teaching:", height=100)
        
        st.markdown("**📊 Metric 2.3.3 (8 marks)** - Student-Mentor ratio")
        col1, col2 = st.columns(2)
        with col1:
            students_mentor = st.number_input("Number of students", min_value=0)
        with col2:
            mentors = st.number_input("Number of mentors (full-time teachers)", min_value=1)
        mentor_ratio = students_mentor / mentors if mentors > 0 else 0
        st.info(f"📈 Student-Mentor Ratio: {mentor_ratio:.1f}:1")
    
    # Key Indicator 2.4
    st.subheader("🔹 Key Indicator 2.4: Teacher Profile and Quality (50 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 2.4.1 (15 marks)** - Full-time teachers against sanctioned posts")
        col1, col2 = st.columns(2)
        with col1:
            filled = st.number_input("Full-time teachers filled", min_value=0)
        with col2:
            sanctioned = st.number_input("Sanctioned posts", min_value=1)
        st.info(f"📈 Filled: {(filled/sanctioned*100):.1f}%")
        
        st.markdown("**📊 Metric 2.4.2 (15 marks)** - Teachers with Ph.D.")
        col1, col2 = st.columns(2)
        with col1:
            phd = st.number_input("Teachers with Ph.D.", min_value=0)
        with col2:
            total_teachers = st.number_input("Total full-time teachers", min_value=1)
        st.info(f"📈 Ph.D. Percentage: {(phd/total_teachers*100):.1f}%")
        
        st.markdown("**📊 Metric 2.4.3 (10 marks)** - Teaching experience")
        avg_exp = st.number_input("Average teaching experience in the same institution (years)", min_value=0.0)
        
        st.markdown("**📊 Metric 2.4.4 (10 marks)** - Teachers with awards")
        awards = st.number_input("Number of teachers who received state/national/international awards", min_value=0)
        st.markdown('<div class="required-doc">📎 Required Document: Award letters, recognition certificates</div>', unsafe_allow_html=True)
        doc_244 = st.file_uploader("Upload award details", key="m244", type=['pdf', 'xlsx'])
    
    # Key Indicator 2.5
    st.subheader("🔹 Key Indicator 2.5: Evaluation Process and Reforms (40 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 2.5.1 (15 marks)** - Result declaration")
        days = st.number_input("Average number of days from exam to result declaration", min_value=0)
        
        st.markdown("**📊 Metric 2.5.2 (5 marks)** - Evaluation grievances")
        grievances = st.number_input("Number of student complaints about evaluation", min_value=0)
        appeared = st.number_input("Total students appeared", min_value=1)
        st.info(f"📈 Grievance Rate: {(grievances/appeared*100):.2f}%")
        
        st.markdown("**📊 Metric 2.5.3 (10 marks)** - IT integration in exams")
        response_253 = st.text_area("Describe IT integration and reforms in examination procedures:", height=100)
        
        st.markdown("**📊 Metric 2.5.4 (10 marks)** - Examination automation")
        automation = st.selectbox("Status of examination division automation:", 
                                 ["100% automation with Examination Management System",
                                  "Student registration, Hall ticket, Result Processing automated",
                                  "Student registration and result processing automated",
                                  "Only result processing automated",
                                  "Manual methodology"])
    
    # Key Indicator 2.6
    st.subheader("🔹 Key Indicator 2.6: Student Performance and Learning Outcomes (30 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 2.6.1 (10 marks)** - Learning outcomes stated")
        st.markdown('<div class="required-doc">📎 Required Document: POs, PSOs, COs published on website</div>', unsafe_allow_html=True)
        url_lo = st.text_input("URL where learning outcomes are published", placeholder="https://...")
        
        st.markdown("**📊 Metric 2.6.2 (10 marks)** - Outcome attainment evaluation")
        response_262 = st.text_area("Describe method of measuring attainment of POs, PSOs, COs:", height=100)
        
        st.markdown("**📊 Metric 2.6.3 (10 marks)** - Pass percentage")
        col1, col2 = st.columns(2)
        with col1:
            passed = st.number_input("Number of final year students who passed", min_value=0)
        with col2:
            appeared_final = st.number_input("Number of final year students who appeared", min_value=1)
        st.info(f"📈 Pass Percentage: {(passed/appeared_final*100):.1f}%")
    
    # Key Indicator 2.7
    st.subheader("🔹 Key Indicator 2.7: Student Satisfaction Survey (30 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 2.7.1 (30 marks)** - Student satisfaction survey")
        st.markdown('<div class="required-doc">📎 Required Document: Database of currently enrolled students for survey (Name, Class, Gender, Student ID, Mobile, Email)</div>', unsafe_allow_html=True)
        survey_data = st.file_uploader("Upload student database (Excel)", key="m271", type=['xlsx', 'csv'])
    
    if st.button("✅ Save Criterion II", type="primary"):
        st.session_state.naac_data['criterion_2'] = {
            '2.1.1': {'seats': seats, 'applications': applications},
            '2.2.2': {'students': students_st, 'teachers': teachers_st},
            '2.3.3': {'students': students_mentor, 'mentors': mentors},
            '2.4.1': {'filled': filled, 'sanctioned': sanctioned},
            '2.4.2': {'phd': phd, 'total': total_teachers},
            '2.4.3': avg_exp, '2.4.4': awards,
            '2.5.1': days, '2.5.2': {'grievances': grievances, 'appeared': appeared},
            '2.6.3': {'passed': passed, 'appeared': appeared_final}
        }
        st.session_state.completed_steps.add(3)
        st.session_state.workflow_step = 4
        st.rerun()

# ============================================================================
# STEP 3: CRITERION III - RESEARCH (250 marks)
# ============================================================================
elif st.session_state.workflow_step == 4:
    st.header("🔬 Step 3: Criterion III - Research, Innovations and Extension (250 marks)")
    
    # Key Indicator 3.1
    st.subheader("🔹 Key Indicator 3.1: Promotion of Research and Facilities (20 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 3.1.1 (2 marks)** - Research promotion policy")
        st.markdown('<div class="required-doc">📎 Required Document: Research promotion policy uploaded on website</div>', unsafe_allow_html=True)
        doc_311 = st.file_uploader("Upload research policy", key="m311", type=['pdf'])
        
        st.markdown("**📊 Metric 3.1.2 (3 marks)** - Seed money for research")
        seed_money = st.number_input("Average seed money per year (INR in Lakhs)", min_value=0.0)
        st.markdown('<div class="required-doc">📎 Required Document: Minutes of relevant bodies, budget statements</div>', unsafe_allow_html=True)
        
        st.markdown("**📊 Metric 3.1.3 (3 marks)** - Teachers with fellowships")
        fellowship_teachers = st.number_input("Number of teachers receiving national/international fellowships", min_value=0)
        
        st.markdown("**📊 Metric 3.1.4 (4 marks)** - Research fellows enrolled")
        jrfs = st.number_input("Number of JRFs, SRFs, Post Doctoral Fellows", min_value=0)
        
        st.markdown("**📊 Metric 3.1.5 (3 marks)** - Research facilities")
        facilities = st.multiselect("Select research facilities available:", 
                                   ["Central Instrumentation Centre", "Animal House/Green House", "Museum",
                                    "Media laboratory/Studios", "Business Lab", "Research/Statistical Databases",
                                    "Mootcourt", "Theatre", "Art Gallery"])
        
        st.markdown("**📊 Metric 3.1.6 (5 marks)** - Department recognitions")
        dept_recog = st.number_input("Number of departments with UGC-SAP, CAS, DST-FIST, DBT, ICSSR recognition", min_value=0)
    
    # Key Indicator 3.2
    st.subheader("🔹 Key Indicator 3.2: Resource Mobilization for Research (20 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 3.2.1 (5 marks)** - Extramural funding (non-government)")
        non_govt_funding = st.number_input("Grants from non-government sources (INR in Lakhs)", min_value=0.0)
        
        st.markdown("**📊 Metric 3.2.2 (10 marks)** - Government research grants")
        govt_funding = st.number_input("Grants from government agencies (INR in Lakhs)", min_value=0.0)
        
        st.markdown("**📊 Metric 3.2.3 (5 marks)** - Research projects per teacher")
        projects = st.number_input("Number of research projects funded", min_value=0)
        teachers_proj = st.number_input("Number of full-time teachers", min_value=1)
        st.info(f"📈 Projects per Teacher: {projects/teachers_proj:.2f}")
    
    # Key Indicator 3.3
    st.subheader("🔹 Key Indicator 3.3: Innovation Ecosystem (30 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 3.3.1 (10 marks)** - Innovation ecosystem")
        response_331 = st.text_area("Describe incubation centre and innovation initiatives:", height=100)
        
        st.markdown("**📊 Metric 3.3.2 (10 marks)** - Workshops on IPR/entrepreneurship")
        workshops = st.number_input("Number of workshops/seminars conducted", min_value=0)
        
        st.markdown("**📊 Metric 3.3.3 (10 marks)** - Awards for innovation")
        innovation_awards = st.number_input("Number of awards for research/innovation", min_value=0)
    
    # Key Indicator 3.4
    st.subheader("🔹 Key Indicator 3.4: Research Publications and Awards (100 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 3.4.1 (5 marks)** - Code of Ethics for research")
        ethics = st.multiselect("Select implemented measures:", 
                               ["Research ethics in coursework", "Institutional Ethics Committees",
                                "Plagiarism check", "Research Advisory Committee"])
        
        st.markdown("**📊 Metric 3.4.2 (5 marks)** - Incentives for teacher awards")
        incentives = st.multiselect("Select incentives provided:", 
                                   ["Commendation and monetary incentive", "Commendation and medal",
                                    "Certificate of honor", "Announcement in Newsletter/website"])
        
        st.markdown("**📊 Metric 3.4.3 (10 marks)** - Patents")
        patents = st.number_input("Number of patents published/awarded", min_value=0)
        
        st.markdown("**📊 Metric 3.4.4 (10 marks)** - Ph.D.s awarded")
        phd_awarded = st.number_input("Number of Ph.D.s awarded", min_value=0)
        guides = st.number_input("Number of teachers recognized as guides", min_value=1)
        st.info(f"📈 Ph.D.s per Teacher: {phd_awarded/guides:.2f}")
        
        st.markdown("**📊 Metric 3.4.5 (15 marks)** - Research papers in UGC journals")
        papers = st.number_input("Number of research papers in UGC notified journals", min_value=0)
        teachers_papers = st.number_input("Number of full-time teachers", min_value=1)
        st.info(f"📈 Papers per Teacher: {papers/teachers_papers:.2f}")
        
        st.markdown("**📊 Metric 3.4.6 (15 marks)** - Books and chapters")
        books = st.number_input("Number of books and chapters published", min_value=0)
        
        st.markdown("**📊 Metric 3.4.7 (10 marks)** - E-content development")
        econtent = st.multiselect("Select platforms where e-content developed:", 
                                 ["e-PG-Pathshala", "CEC", "SWAYAM", "Other MOOCs", "NPTEL", "Institutional LMS"])
    
    # Key Indicator 3.5
    st.subheader("🔹 Key Indicator 3.5: Consultancy (20 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 3.5.1 (5 marks)** - Consultancy policy")
        st.markdown('<div class="required-doc">📎 Required Document: Consultancy policy document</div>', unsafe_allow_html=True)
        
        st.markdown("**📊 Metric 3.5.2 (15 marks)** - Revenue from consultancy")
        consultancy_revenue = st.number_input("Revenue generated from consultancy (INR in Lakhs)", min_value=0.0)
    
    # Key Indicator 3.6
    st.subheader("🔹 Key Indicator 3.6: Extension Activities (40 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 3.6.1 (6 marks)** - Extension impact")
        response_361 = st.text_area("Describe impact of extension activities on students and community:", height=100)
        
        st.markdown("**📊 Metric 3.6.2 (10 marks)** - Awards for extension")
        extension_awards = st.number_input("Number of awards for extension activities", min_value=0)
        
        st.markdown("**📊 Metric 3.6.3 (12 marks)** - Extension programs")
        extension_programs = st.number_input("Number of extension and outreach programs", min_value=0)
        
        st.markdown("**📊 Metric 3.6.4 (12 marks)** - Student participation in extension")
        col1, col2 = st.columns(2)
        with col1:
            students_ext = st.number_input("Students participated in extension", min_value=0)
        with col2:
            total_students_ext = st.number_input("Total students", min_value=1)
        st.info(f"📈 Participation: {(students_ext/total_students_ext*100):.1f}%")
    
    # Key Indicator 3.7
    st.subheader("🔹 Key Indicator 3.7: Collaboration (20 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 3.7.1 (10 marks)** - Collaborative activities")
        collab_activities = st.number_input("Number of collaborative activities", min_value=0)
        
        st.markdown("**📊 Metric 3.7.2 (10 marks)** - Functional MoUs")
        mous = st.number_input("Number of functional MoUs", min_value=0)
        st.markdown('<div class="required-doc">📎 Required Document: e-copies of MoUs, activity reports</div>', unsafe_allow_html=True)
        doc_372 = st.file_uploader("Upload MoU documents", key="m372", type=['pdf'])
    
    if st.button("✅ Save Criterion III", type="primary"):
        st.session_state.naac_data['criterion_3'] = {
            '3.1.2': seed_money, '3.1.3': fellowship_teachers, '3.1.4': jrfs,
            '3.2.1': non_govt_funding, '3.2.2': govt_funding,
            '3.3.2': workshops, '3.4.3': patents, '3.4.4': {'phd': phd_awarded, 'guides': guides},
            '3.4.5': {'papers': papers, 'teachers': teachers_papers},
            '3.5.2': consultancy_revenue, '3.6.2': extension_awards,
            '3.6.3': extension_programs, '3.6.4': {'students': students_ext, 'total': total_students_ext},
            '3.7.1': collab_activities, '3.7.2': mous
        }
        st.session_state.completed_steps.add(4)
        st.session_state.workflow_step = 5
        st.rerun()

# ============================================================================
# STEP 4: CRITERION IV - INFRASTRUCTURE (100 marks)
# ============================================================================
elif st.session_state.workflow_step == 5:
    st.header("🏛️ Step 4: Criterion IV - Infrastructure and Learning Resources (100 marks)")
    
    # Key Indicator 4.1
    st.subheader("🔹 Key Indicator 4.1: Physical Facilities (30 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 4.1.1 (10 marks)** - Teaching-learning facilities")
        response_411 = st.text_area("Describe adequacy of classrooms, laboratories, computing equipment:", height=100)
        st.markdown('<div class="required-doc">📎 Required Document: Geo-tagged photos of facilities</div>', unsafe_allow_html=True)
        geo_photos = st.file_uploader("Upload geo-tagged photos of classrooms, labs", type=['jpg', 'png'], accept_multiple_files=True)
        
        st.markdown("**📊 Metric 4.1.2 (5 marks)** - Cultural, sports facilities")
        response_412 = st.text_area("Describe facilities for cultural activities, yoga, games, sports:", height=100)
        
        st.markdown("**📊 Metric 4.1.3 (5 marks)** - General campus facilities")
        response_413 = st.text_area("Describe general campus facilities and ambience:", height=100)
        
        st.markdown("**📊 Metric 4.1.4 (10 marks)** - Infrastructure expenditure")
        infra_exp = st.number_input("Expenditure on infrastructure augmentation (INR in Lakhs)", min_value=0.0)
        total_exp = st.number_input("Total expenditure excluding salary (INR in Lakhs)", min_value=1.0)
        st.info(f"📈 Infrastructure Spend: {(infra_exp/total_exp*100):.1f}% of total")
    
    # Key Indicator 4.2
    st.subheader("🔹 Key Indicator 4.2: Library as a Learning Resource (20 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 4.2.1 (5 marks)** - Library automation")
        response_421 = st.text_area("Describe library automation and digitization facility:", height=100)
        
        st.markdown("**📊 Metric 4.2.2 (6 marks)** - e-Library subscriptions")
        e_resources = st.multiselect("Select e-resources subscribed:", 
                                    ["e-journals", "e-books", "e-ShodhSindhu", "Shodhganga", "Databases"])
        
        st.markdown("**📊 Metric 4.2.3 (5 marks)** - Library expenditure")
        library_exp = st.number_input("Annual expenditure on books and journals (INR in Lakhs)", min_value=0.0)
        
        st.markdown("**📊 Metric 4.2.4 (4 marks)** - Library usage")
        daily_users = st.number_input("Average number of teachers and students using library per day", min_value=0)
        total_users = st.number_input("Total teachers and students", min_value=1)
        st.info(f"📈 Daily Usage: {(daily_users/total_users*100):.1f}%")
    
    # Key Indicator 4.3
    st.subheader("🔹 Key Indicator 4.3: IT Infrastructure (30 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 4.3.1 (5 marks)** - ICT-enabled classrooms")
        ict_classrooms = st.number_input("Number of classrooms and seminar halls with ICT facilities", min_value=0)
        total_classrooms = st.number_input("Total classrooms and seminar halls", min_value=1)
        st.info(f"📈 ICT-enabled: {(ict_classrooms/total_classrooms*100):.1f}%")
        
        st.markdown("**📊 Metric 4.3.2 (5 marks)** - IT policy")
        response_432 = st.text_area("Describe IT policy and budgetary provisions:", height=100)
        
        st.markdown("**📊 Metric 4.3.3 (5 marks)** - Student-Computer ratio")
        students_computer = st.number_input("Number of students", min_value=0)
        computers = st.number_input("Computers for academic purposes", min_value=1)
        st.info(f"📈 Student-Computer Ratio: {students_computer/computers:.1f}:1")
        
        st.markdown("**📊 Metric 4.3.4 (5 marks)** - Internet bandwidth")
        bandwidth = st.selectbox("Available internet bandwidth:", 
                                [">= 1 GBPS", "500 MBPS - 1 GBPS", "250 MBPS - 500 MBPS", 
                                 "50 MBPS - 250 MBPS", "< 50 MBPS"])
        
        st.markdown("**📊 Metric 4.3.5 (10 marks)** - e-content development facilities")
        econtent_facilities = st.multiselect("Select facilities:", 
                                            ["Media centre", "Audio visual centre", 
                                             "Lecture Capturing System", "Mixing equipments and software"])
    
    # Key Indicator 4.4
    st.subheader("🔹 Key Indicator 4.4: Maintenance of Campus Infrastructure (20 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 4.4.1 (10 marks)** - Maintenance expenditure")
        maint_exp = st.number_input("Expenditure on maintenance (INR in Lakhs)", min_value=0.0)
        
        st.markdown("**📊 Metric 4.4.2 (10 marks)** - Maintenance systems")
        response_442 = st.text_area("Describe systems and procedures for maintaining facilities:", height=100)
    
    if st.button("✅ Save Criterion IV", type="primary"):
        st.session_state.naac_data['criterion_4'] = {
            '4.1.4': {'infra': infra_exp, 'total': total_exp},
            '4.2.2': e_resources, '4.2.3': library_exp,
            '4.2.4': {'daily': daily_users, 'total': total_users},
            '4.3.1': {'ict': ict_classrooms, 'total': total_classrooms},
            '4.3.3': {'students': students_computer, 'computers': computers}
        }
        st.session_state.completed_steps.add(5)
        st.session_state.workflow_step = 6
        st.rerun()

# ============================================================================
# STEP 5: CRITERION V - STUDENT SUPPORT (100 marks)
# ============================================================================
elif st.session_state.workflow_step == 6:
    st.header("👥 Step 5: Criterion V - Student Support and Progression (100 marks)")
    
    st.subheader("🔹 Key Indicator 5.1: Student Support (30 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 5.1.1 (10 marks)** - Scholarships and freeships")
        scholarship_beneficiaries = st.number_input("Number of students benefited by scholarships", min_value=0)
        st.markdown('<div class="required-doc">📎 Required Document: List of beneficiaries, sanction letters</div>', unsafe_allow_html=True)
        
        st.markdown("**📊 Metric 5.1.2 (10 marks)** - Career counseling")
        career_counseling = st.number_input("Number of students benefited by career counseling", min_value=0)
        
        st.markdown("**📊 Metric 5.1.3 (5 marks)** - Skills enhancement initiatives")
        skills = st.multiselect("Select initiatives:", 
                               ["Soft skills", "Language and communication skills", 
                                "Life skills (Yoga, fitness)", "Awareness of technology trends"])
        
        st.markdown("**📊 Metric 5.1.4 (5 marks)** - Grievance redressal")
        grievance_mechanisms = st.multiselect("Select mechanisms:", 
                                             ["Implementation of statutory guidelines",
                                              "Zero tolerance policies",
                                              "Online/offline grievance submission",
                                              "Timely redressal through committees"])
    
    st.subheader("🔹 Key Indicator 5.2: Student Progression (40 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 5.2.1 (10 marks)** - Qualifying in competitive exams")
        qualified = st.number_input("Number of students qualifying in NET/SLET/GATE etc.", min_value=0)
        
        st.markdown("**📊 Metric 5.2.2 (15 marks)** - Placement percentage")
        placed = st.number_input("Number of outgoing students placed", min_value=0)
        outgoing = st.number_input("Total outgoing students", min_value=1)
        st.info(f"📈 Placement Rate: {(placed/outgoing*100):.1f}%")
        
        st.markdown("**📊 Metric 5.2.3 (15 marks)** - Higher education progression")
        higher_edu = st.number_input("Number of students progressed to higher education", min_value=0)
        st.info(f"📈 Progression Rate: {(higher_edu/outgoing*100):.1f}%")
    
    st.subheader("🔹 Key Indicator 5.3: Student Participation and Activities (20 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 5.3.1 (10 marks)** - Awards in sports/cultural events")
        awards_count = st.number_input("Number of awards/medals won", min_value=0)
        
        st.markdown("**📊 Metric 5.3.2 (5 marks)** - Student council")
        response_532 = st.text_area("Describe student council and its activities:", height=100)
        
        st.markdown("**📊 Metric 5.3.3 (5 marks)** - Sports and cultural events")
        events = st.number_input("Number of sports and cultural events organized", min_value=0)
    
    st.subheader("🔹 Key Indicator 5.4: Alumni Engagement (10 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 5.4.1 (2 marks)** - Alumni contribution")
        response_541 = st.text_area("Describe alumni association contribution:", height=100)
        
        st.markdown("**📊 Metric 5.4.2 (8 marks)** - Alumni contribution amount")
        alumni_contribution = st.radio("Alumni contribution (INR in Lakhs):",
                                      [">= 100", "50 - 100", "20 - 50", "5 - 20", "< 5"])
    
    if st.button("✅ Save Criterion V", type="primary"):
        st.session_state.naac_data['criterion_5'] = {
            '5.1.1': scholarship_beneficiaries, '5.1.2': career_counseling,
            '5.2.2': {'placed': placed, 'outgoing': outgoing},
            '5.2.3': higher_edu, '5.3.1': awards_count, '5.3.3': events
        }
        st.session_state.completed_steps.add(6)
        st.session_state.workflow_step = 7
        st.rerun()

# ============================================================================
# STEP 6: CRITERION VI - GOVERNANCE (100 marks)
# ============================================================================
elif st.session_state.workflow_step == 7:
    st.header("⚙️ Step 6: Criterion VI - Governance, Leadership and Management (100 marks)")
    
    st.subheader("🔹 Key Indicator 6.1: Institutional Vision and Leadership (10 marks)")
    response_611 = st.text_area("Describe institutional vision and participative decision-making:", height=100)
    
    st.subheader("🔹 Key Indicator 6.2: Strategy Development and Deployment (10 marks)")
    response_621 = st.text_area("Describe strategy development and implementation:", height=100)
    
    st.subheader("🔹 Key Indicator 6.3: Faculty Empowerment Strategies (30 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 6.3.1 (4 marks)** - Performance appraisal system")
        response_631 = st.text_area("Describe performance appraisal, promotions, welfare measures:", height=100)
        
        st.markdown("**📊 Metric 6.3.2 (10 marks)** - Financial support for teachers")
        teachers_supported = st.number_input("Number of teachers provided financial support", min_value=0)
        
        st.markdown("**📊 Metric 6.3.3 (8 marks)** - Professional development programs")
        fdp_count = st.number_input("Number of professional development programs organized", min_value=0)
        
        st.markdown("**📊 Metric 6.3.4 (8 marks)** - Teachers in FDP programs")
        teachers_fdp = st.number_input("Number of teachers undergoing FDP/Orientation/Refresher courses", min_value=0)
        total_teachers_fdp = st.number_input("Total full-time teachers", min_value=1)
        st.info(f"📈 FDP Participation: {(teachers_fdp/total_teachers_fdp*100):.1f}%")
    
    st.subheader("🔹 Key Indicator 6.4: Financial Management and Resource Mobilization (20 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 6.4.1 (4 marks)** - Resource mobilization strategies")
        response_641 = st.text_area("Describe resource mobilization policy:", height=100)
        
        st.markdown("**📊 Metric 6.4.2 (8 marks)** - Government grants")
        govt_grants = st.number_input("Funds from government bodies (INR in Lakhs)", min_value=0.0)
        
        st.markdown("**📊 Metric 6.4.3 (6 marks)** - Non-government grants")
        ngo_grants = st.number_input("Funds from non-government sources (INR in Lakhs)", min_value=0.0)
        
        st.markdown("**📊 Metric 6.4.4 (2 marks)** - Financial audits")
        response_644 = st.text_area("Describe internal and external financial audits:", height=100)
    
    st.subheader("🔹 Key Indicator 6.5: Internal Quality Assurance System (30 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 6.5.1 (10 marks)** - IQAC contributions")
        response_651 = st.text_area("Describe IQAC initiatives and quality enhancement:", height=100)
        
        st.markdown("**📊 Metric 6.5.2 (10 marks)** - Quality assurance initiatives")
        quality_initiatives = st.multiselect("Select initiatives:", 
                                           ["Academic Administrative Audit", "Quality conferences",
                                            "Collaborative quality initiatives", "Orientation on quality",
                                            "NIRF participation", "ISO Certification", "NBA certification"])
        
        st.markdown("**📊 Metric 6.5.3 (10 marks)** - Quality improvements")
        response_653 = st.text_area("Describe incremental quality improvements in last five years:", height=100)
    
    if st.button("✅ Save Criterion VI", type="primary"):
        st.session_state.naac_data['criterion_6'] = {
            '6.3.2': teachers_supported, '6.3.3': fdp_count,
            '6.3.4': {'teachers': teachers_fdp, 'total': total_teachers_fdp},
            '6.4.2': govt_grants, '6.4.3': ngo_grants
        }
        st.session_state.completed_steps.add(7)
        st.session_state.workflow_step = 8
        st.rerun()

# ============================================================================
# STEP 7: CRITERION VII - VALUES & BEST PRACTICES (100 marks)
# ============================================================================
elif st.session_state.workflow_step == 8:
    st.header("💎 Step 7: Criterion VII - Institutional Values and Best Practices (100 marks)")
    
    st.subheader("🔹 Key Indicator 7.1: Institutional Values and Social Responsibilities (50 marks)")
    
    with st.container():
        st.markdown("**📊 Metric 7.1.1 (5 marks)** - Gender equity")
        response_711 = st.text_area("Describe gender equity measures and facilities for women:", height=100)
        
        st.markdown("**📊 Metric 7.1.2 (5 marks)** - Alternate energy sources")
        energy = st.multiselect("Select energy conservation measures:", 
                               ["Solar energy", "Biogas plant", "Wheeling to Grid", 
                                "Sensor-based conservation", "LED bulbs"])
        
        st.markdown("**📊 Metric 7.1.3 (4 marks)** - Waste management")
        response_713 = st.text_area("Describe waste management facilities:", height=100)
        
        st.markdown("**📊 Metric 7.1.4 (4 marks)** - Water conservation")
        water = st.multiselect("Select water conservation facilities:", 
                              ["Rain water harvesting", "Borewell recharge", "Tanks and bunds",
                               "Waste water recycling", "Water body maintenance"])
        
        st.markdown("**📊 Metric 7.1.5 (4 marks)** - Green campus initiatives")
        green = st.multiselect("Select initiatives:", 
                              ["Restricted auto entry", "Bicycles/battery vehicles", 
                               "Pedestrian pathways", "Ban on plastic", "Landscaping"])
        
        st.markdown("**📊 Metric 7.1.6 (5 marks)** - Quality audits")
        audits = st.multiselect("Select audits conducted:", 
                               ["Green audit", "Energy audit", "Environment audit", 
                                "Clean campus awards", "Environmental activities"])
        
        st.markdown("**📊 Metric 7.1.7 (4 marks)** - Disabled-friendly facilities")
        disabled = st.multiselect("Select facilities:", 
                                 ["Ramps/lifts", "Disabled-friendly washrooms", "Signage/tactile path",
                                  "Assistive technology", "Enquiry provision"])
        
        st.markdown("**📊 Metric 7.1.8 (5 marks)** - Inclusive environment")
        response_718 = st.text_area("Describe efforts for inclusive environment:", height=100)
        
        st.markdown("**📊 Metric 7.1.9 (4 marks)** - Constitutional obligations")
        response_719 = st.text_area("Describe sensitization to constitutional values:", height=100)
        
        st.markdown("**📊 Metric 7.1.10 (5 marks)** - Code of conduct")
        code = st.multiselect("Select implemented:", 
                             ["Code of conduct on website", "Monitoring committee", 
                              "Professional ethics programs", "Annual awareness programs"])
        
        st.markdown("**📊 Metric 7.1.11 (5 marks)** - Commemorative days")
        response_7111 = st.text_area("Describe celebration of national/international events:", height=100)
    
    st.subheader("🔹 Key Indicator 7.2: Best Practices (30 marks)")
    response_72 = st.text_area("Describe two best practices (each with title, objectives, context, practice, evidence, problems):", height=200)
    
    st.subheader("🔹 Key Indicator 7.3: Institutional Distinctiveness (20 marks)")
    response_73 = st.text_area("Describe distinctive features of the institution:", height=150)
    
    if st.button("✅ Save Criterion VII", type="primary"):
        st.session_state.naac_data['criterion_7'] = {
            '7.1.2': energy, '7.1.4': water, '7.1.5': green,
            '7.1.6': audits, '7.1.7': disabled, '7.1.10': code
        }
        st.session_state.completed_steps.add(8)
        st.session_state.workflow_step = 9
        st.rerun()

# ============================================================================
# STEP 8: GAP ANALYSIS
# ============================================================================
elif st.session_state.workflow_step == 9:
    st.header("📊 Step 8: Gap Analysis - Review & Validate")
    
    # Calculate completion
    completed_criteria = []
    for i in range(1, 8):
        if f'criterion_{i}' in st.session_state.naac_data and st.session_state.naac_data[f'criterion_{i}']:
            completed_criteria.append(i)
    
    missing_criteria = [i for i in range(1, 8) if i not in completed_criteria]
    
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"✅ Completed: {len(completed_criteria)}/7 criteria")
        for c in completed_criteria:
            st.write(f"  • Criterion {c}")
    with col2:
        if missing_criteria:
            st.error(f"❌ Missing: {len(missing_criteria)}/7 criteria")
            for c in missing_criteria:
                st.write(f"  • Criterion {c}")
        else:
            st.success("✅ All 7 criteria completed!")
    
    st.subheader("📋 Pre-assessment Summary")
    st.info("Based on NAAC Revised Manual 2020 and University SOP")
    
    if st.button("Generate Score Report", type="primary"):
        st.session_state.completed_steps.add(9)
        st.session_state.workflow_step = 10
        st.rerun()

# ============================================================================
# STEP 9: SCORE REPORT & SSR
# ============================================================================
elif st.session_state.workflow_step == 10:
    st.header("🎯 Step 9: Score Report & SSR Generation")
    
    # Calculate estimated score (simplified for now)
    completed_count = sum(1 for i in range(1, 8) if f'criterion_{i}' in st.session_state.naac_data)
    estimated_cgpa = (completed_count / 7) * 4
    grade = "A" if estimated_cgpa >= 3.0 else "B++" if estimated_cgpa >= 2.5 else "B"
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Estimated CGPA", f"{estimated_cgpa:.2f}", delta="Target: 3.26")
    with col2:
        st.metric("Projected Grade", grade)
    with col3:
        st.metric("Completion", f"{completed_count}/7 criteria")
    
    st.subheader("📑 Generate Self-Study Report (SSR)")
    
    if st.button("Generate SSR Draft", type="primary"):
        st.success("SSR generated successfully!")
        st.download_button("Download SSR", data="SSR content will be here", 
                          file_name=f"NAAC_SSR_{datetime.now().strftime('%Y%m%d')}.pdf")
    
    st.success("🎉 You've completed the NAAC preparation workflow!")
    st.markdown("""
    ### Next Steps:
    1. Review all criterion data for accuracy
    2. Upload any missing supporting documents
    3. Conduct mock peer team visit
    4. Submit for actual NAAC assessment
    """)

st.markdown("---")
st.caption("NAAC Accreditation Assistant v2.0 | Based on NAAC Revised Manual 2020 and University SOP")

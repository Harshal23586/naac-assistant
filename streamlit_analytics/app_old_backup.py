# app.py - Main Application with Full-Width Layout and NAAC Module
import streamlit as st

# ============================================================================
# MUST BE THE FIRST STREAMLIT COMMAND - PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="SUGAM - Smart Unified Governance and Approval Management",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS FOR FULL-WIDTH LAYOUT
# ============================================================================
st.markdown("""
<style>
    /* Remove padding from main container */
    .main > div {
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
    }
    
    /* Main container full width */
    .main .block-container {
        max-width: 100% !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        padding-top: 1rem;
        padding-bottom: 2rem;
    }
    
    /* Remove left and right white space */
    section.main {
        padding-left: 0 !important;
        padding-right: 0 !important;
    }
    
    /* Full width app */
    .stApp {
        max-width: 100%;
    }
    
    /* Make sidebar properly sized */
    [data-testid="stSidebar"] {
        padding-left: 0.5rem;
        padding-right: 0.5rem;
        min-width: 250px;
        max-width: 300px;
    }
    
    /* Sidebar collapsed mode */
    section[data-testid="stSidebar"][aria-expanded="false"] + section.main {
        width: 100% !important;
    }
    
    /* Horizontal blocks full width */
    .stHorizontalBlock {
        gap: 1rem;
        width: 100%;
        flex-wrap: wrap;
    }
    
    /* Columns to fill space */
    [data-testid="column"] {
        min-width: 200px;
        flex: 1 1 0% !important;
    }
    
    /* Metrics cards */
    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
    }
    
    /* Dataframes full width */
    .stDataFrame, .stTable {
        width: 100%;
        overflow-x: auto;
    }
    
    /* Plotly charts full width */
    .js-plotly-plot, .plotly-graph-div {
        width: 100% !important;
    }
    
    /* Expanders full width */
    .streamlit-expanderHeader {
        width: 100%;
    }
    
    /* Remove extra margins */
    .element-container {
        width: 100%;
    }
    
    /* Responsive columns */
    .row-widget.stHorizontalBlock {
        flex-wrap: wrap;
    }
    
    /* For better spacing on wide screens */
    @media (min-width: 1400px) {
        .main .block-container {
            padding-left: 3rem !important;
            padding-right: 3rem !important;
        }
    }
    
    /* For mobile devices */
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
        }
        
        [data-testid="column"] {
            min-width: 100%;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# IMPORTS
# ============================================================================
import sys
import os
from datetime import datetime
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import existing modules
from core.analyzer import InstitutionalAIAnalyzer
from modules.dashboard import create_performance_dashboard
from modules.document_analysis import create_document_analysis_module
from modules.intelligence_hub import create_institutional_intelligence_hub
from modules.data_management import create_data_management_module
from modules.api_documentation import create_api_documentation
from modules.pdf_reports import create_pdf_report_module
from modules.system_settings import create_system_settings
from modules.rag_dashboard import create_rag_dashboard
from modules.decision_tree_classifier import create_decision_tree_module

# Import NAAC modules
from config.naac_config import CRITERION_WEIGHTAGES, GRADE_THRESHOLDS, METRICS
from modules.naac.criteria_forms import create_criteria_forms
from modules.naac.scoring_engine import NAACScoringEngine
from modules.naac.gap_analysis import create_gap_analysis
from modules.naac.report_generator import generate_ssr

# Try to import RAG validation
try:
    from modules.rag_core import create_rag_validation_dashboard
    RAG_VALIDATION_AVAILABLE = True
except Exception as e:
    RAG_VALIDATION_AVAILABLE = False
    def create_rag_validation_dashboard(analyzer):
        st.error("RAG Validation module is not available. Please check the module configuration.")

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
if 'institution_user' not in st.session_state:
    st.session_state.institution_user = None
if 'user_role' not in st.session_state:
    st.session_state.user_role = None
if 'ugc_aicte_user' not in st.session_state:
    st.session_state.ugc_aicte_user = None
if 'naac_responses' not in st.session_state:
    st.session_state.naac_responses = {}
if 'institution_name' not in st.session_state:
    st.session_state.institution_name = "Sample Institution"
if 'cycle' not in st.session_state:
    st.session_state.cycle = 1

# ============================================================================
# PREDICTION FUNCTION
# ============================================================================
def predict_performance_tab(analyzer):
    """Tab for predicting 5-year performance using logistic regression"""
    st.header("📊 Institutional Performance Prediction (Logistic Regression)")
    
    # Load data
    data = analyzer.historical_data.copy()
    
    # Define available parameters
    all_parameters = [
        'student_faculty_ratio', 'phd_faculty_ratio', 'research_publications',
        'research_grants_amount', 'patents_filed', 'industry_collaborations',
        'digital_infrastructure_score', 'library_volumes', 'laboratory_equipment_score',
        'financial_stability_score', 'compliance_score', 'administrative_efficiency',
        'placement_rate', 'higher_education_rate', 'entrepreneurship_cell_score',
        'community_projects', 'rural_outreach_score', 'inclusive_education_index'
    ]
    
    def get_target_label(recommendation):
        if 'Provisional' in recommendation or 'Conditional' in recommendation:
            return 1
        elif 'Approval' in recommendation:
            return 1
        elif 'Rejection' in recommendation:
            return 0
        else:
            return 0
    
    # Create training data
    train_data = []
    for inst_id in data['institution_id'].unique():
        inst_data = data[data['institution_id'] == inst_id].sort_values('year')
        if len(inst_data) >= 6:
            for i in range(len(inst_data) - 5):
                window_data = inst_data.iloc[i:i+5]
                features = {}
                for param in all_parameters:
                    features[param] = window_data[param].mean()
                future_data = inst_data.iloc[i+5:min(i+10, len(inst_data))]
                if len(future_data) > 0:
                    future_labels = future_data['approval_recommendation'].apply(get_target_label)
                    target = 1 if future_labels.mean() > 0.5 else 0
                    features['institution_id'] = inst_id
                    features['start_year'] = window_data['year'].min()
                    features['end_year'] = window_data['year'].max()
                    features['target'] = target
                    train_data.append(features)
    
    if not train_data:
        st.error("Insufficient data for prediction. Need more historical data.")
        return
    
    train_df = pd.DataFrame(train_data)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Samples", len(train_df))
    with col2:
        good_perf = train_df['target'].sum()
        st.metric("Good Performance Samples", good_perf)
    with col3:
        poor_perf = len(train_df) - good_perf
        st.metric("Poor Performance Samples", poor_perf)
    
    # Parameter selection
    st.subheader("🎯 Select Parameters for Prediction")
    selected_params = st.multiselect(
        "Choose parameters for the prediction model:",
        all_parameters,
        default=all_parameters[:8]
    )
    
    if not selected_params:
        st.warning("Please select at least one parameter for prediction.")
        return
    
    # Train model
    st.subheader("🤖 Model Training")
    X = train_df[selected_params]
    y = train_df['target']
    
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import accuracy_score
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train_scaled, y_train)
    
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Model Accuracy", f"{accuracy:.2%}")
    with col2:
        st.metric("Training Samples", len(X_train))
    with col3:
        st.metric("Test Samples", len(X_test))
    
    # Feature importance
    st.subheader("📊 Feature Importance")
    feature_importance = pd.DataFrame({
        'Feature': selected_params,
        'Coefficient': model.coef_[0]
    }).sort_values('Coefficient', key=abs, ascending=False)
    st.dataframe(feature_importance, use_container_width=True)
    
    # Prediction section
    st.subheader("🔮 Predict Future Performance")
    institutions = sorted(data['institution_id'].unique())
    selected_institution = st.selectbox("Select Institution to Predict:", institutions, index=0)
    
    inst_data = data[data['institution_id'] == selected_institution].sort_values('year', ascending=False)
    
    if len(inst_data) < 5:
        st.warning(f"Selected institution needs at least 5 years of data. Currently has {len(inst_data)} years.")
        return
    
    latest_5_years = inst_data.head(5).sort_values('year')
    st.info(f"**Institution:** {inst_data.iloc[0]['institution_name']} ({selected_institution})")
    
    prediction_features = {}
    for param in selected_params:
        if param in latest_5_years.columns:
            prediction_features[param] = latest_5_years[param].mean()
        else:
            prediction_features[param] = 0
    
    prediction_df = pd.DataFrame([prediction_features])
    prediction_scaled = scaler.transform(prediction_df)
    prediction = model.predict(prediction_scaled)[0]
    prediction_proba = model.predict_proba(prediction_scaled)[0]
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📋 Input Data (Last 5 Years Average)")
        display_df = latest_5_years[['year'] + selected_params[:5]]
        st.dataframe(display_df, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Prediction Results")
        if prediction == 1:
            st.success("✅ **Prediction: GOOD PERFORMANCE**")
        else:
            st.error("❌ **Prediction: POOR PERFORMANCE**")
        
        st.subheader("📊 Prediction Confidence")
        prob_good = prediction_proba[1] * 100
        prob_poor = prediction_proba[0] * 100
        
        col_prob1, col_prob2 = st.columns(2)
        with col_prob1:
            st.metric("Good Performance Probability", f"{prob_good:.1f}%")
        with col_prob2:
            st.metric("Poor Performance Probability", f"{prob_poor:.1f}%")
        
        st.progress(prob_good/100, text=f"Good Performance Confidence: {prob_good:.1f}%")

# ============================================================================
# MAIN FUNCTION
# ============================================================================
def main():
    """Main application entry point"""
    
    # Check if institution user is logged in
    if st.session_state.institution_user is not None:
        try:
            analyzer = InstitutionalAIAnalyzer()
            user_info = {
                'username': st.session_state.institution_user,
                'role': 'institution',
                'institution_id': 'INST001',
                'name': st.session_state.institution_name
            }
            from institution.dashboard import create_institution_dashboard
            create_institution_dashboard(analyzer, user_info)
            
            if st.sidebar.button("🚪 Logout"):
                st.session_state.institution_user = None
                st.session_state.user_role = None
                st.rerun()
            return
        except Exception as e:
            st.error(f"❌ System initialization error: {str(e)}")
            st.session_state.institution_user = None
            st.session_state.user_role = None
    
    # Check if UGC/AICTE user is logged in
    if st.session_state.ugc_aicte_user is not None:
        try:
            analyzer = InstitutionalAIAnalyzer()
            show_main_application(analyzer)
            return
        except Exception as e:
            st.error(f"❌ System initialization error: {str(e)}")
            st.session_state.ugc_aicte_user = None
            st.session_state.user_role = None
    
    # Show landing page
    show_landing_page()

def show_landing_page():
    """Display the clean landing page with authentication options"""
    
    # Main header
    col1, col2 = st.columns([1, 4])
    
    with col1:
        st.markdown("""
        <div style="width: 150px; height: 150px; background-color: #0047AB; 
                    color: white; display: flex; align-items: center; 
                    justify-content: center; border-radius: 10px; font-size: 32px;">
            <strong>SUGAM</strong>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<h1 class="main-header">सुगम - SUGAM - Smart Unified Governance and Approval Management</h1>', unsafe_allow_html=True)
        st.markdown('<h3 class="sub-header">UGC & AICTE - Institutional Performance Tracking & Decision Support</h3>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style='padding: 20px; background-color: #f0f7ff; border-radius: 10px; margin-bottom: 20px;'>
        <h4>🏛️ National Education Policy 2020 (NEP 2020) Implementation Platform</h4>
        <p>This AI-powered platform supports the transformative reforms for strengthening assessment and 
        accreditation of Higher Education Institutions in India.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("📋 Key Features")
        features = [
            "✅ **Binary Accreditation System**: 'Accredited', 'Awaiting Accreditation', 'Not Accredited'",
            "✅ **Level-Based Excellence**: Institutions graded from Level 1 to Level 5",
            "✅ **Unified Data Platform**: 'One Nation One Data' architecture",
            "✅ **Technology-Driven Assessment**: AI and automation",
            "✅ **AI Performance Prediction**: Predict 5-year institutional performance",
            "✅ **NAAC Accreditation Assistant**: Complete NAAC preparation tool with 7 criteria"
        ]
        for feature in features:
            st.markdown(feature)
    
    with col2:
        st.markdown("""
        <div style='padding: 20px; background-color: #fff3cd; border-radius: 10px; margin-bottom: 20px;'>
        <h4>🔐 Secure Access</h4>
        <p>Authorized access only for registered institutions and UGC/AICTE personnel.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("🇮🇳 Indian HEI Landscape")
        stats = {
            "Total HEIs in India": "50,000+",
            "NAAC Accredited Universities": "~36.67%",
            "NAAC Accredited Colleges": "~21.64%",
            "IITs in Global Rankings": "8 in Top 400"
        }
        for key, value in stats.items():
            st.metric(key, value)
    
    # Authentication Section
    st.markdown("---")
    st.subheader("🔐 System Access")
    
    login_col1, login_col2 = st.columns(2)
    
    with login_col1:
        st.markdown("### 🏫 Institution Login")
        
        with st.form("institution_login", clear_on_submit=False):
            inst_username = st.text_input("Username", placeholder="Enter institution username")
            inst_password = st.text_input("Password", type="password", placeholder="Enter password")
            inst_submit = st.form_submit_button("✅ Login as Institution")
            
            if inst_submit:
                if inst_username == "institute" and inst_password == "Institute123":
                    st.session_state.institution_user = inst_username
                    st.session_state.user_role = "Institution"
                    st.success("✅ Login successful! Redirecting...")
                    st.rerun()
                else:
                    st.error("❌ Invalid credentials. Use: institute / Institute123")
    
    with login_col2:
        st.markdown("### 🏛️ UGC/AICTE Login")
        
        with st.form("ugc_aicte_login", clear_on_submit=False):
            ugc_username = st.text_input("Username", placeholder="Enter UGC/AICTE username")
            ugc_password = st.text_input("Password", type="password", placeholder="Enter password")
            ugc_submit = st.form_submit_button("✅ Login as UGC/AICTE")
            
            if ugc_submit:
                if ugc_username == "ugc123" and ugc_password == "Ugc123456":
                    st.session_state.ugc_aicte_user = ugc_username
                    st.session_state.user_role = "UGC/AICTE Officer"
                    st.success("✅ Login successful! Redirecting...")
                    st.rerun()
                else:
                    st.error("❌ Invalid credentials. Use: ugc123 / Ugc123456")
    
    st.markdown("---")
    st.markdown(f"""
    <div style='text-align: center; color: #6c757d;'>
    <p><strong>Based on Dr. Radhakrishnan Committee Report</strong> | Ministry of Education, Government of India</p>
    <p>SUGAM Platform v2.0 | Access restricted to authorized personnel | {datetime.now().strftime("%d %B %Y")}</p>
    </div>
    """, unsafe_allow_html=True)

def show_main_application(analyzer):
    """Show the main application after UGC/AICTE login"""
    
    # Display system stats in sidebar
    try:
        total_institutions = analyzer.historical_data['institution_id'].nunique()
        total_years = analyzer.historical_data['year'].nunique()
        total_records = len(analyzer.historical_data)
        
        st.sidebar.success(f"📊 Data: {total_institutions} institutes × {total_years} years")
        st.sidebar.info(f"📈 Total Records: {total_records}")
    except Exception as e:
        st.sidebar.error(f"⚠️ Data verification issue: {str(e)}")
    
    # Sidebar navigation
    st.sidebar.title("🧭 Navigation Panel")
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**👤 Logged in as:** {st.session_state.user_role}")
    
    if st.sidebar.button("🚪 Logout"):
        st.session_state.ugc_aicte_user = None
        st.session_state.user_role = None
        st.rerun()
    
    st.sidebar.markdown("### AI Modules")

      
    app_mode = st.sidebar.selectbox(
        "Select Analysis Module",
        [
            "🏛️ NAAC Accreditation Assistant",
            "📊 Performance Dashboard",
            "📋 Document Analysis",
            "🤖 Intelligence Hub",
            "🔍 RAG Data Management",
            "📋 NAAC Accreditation Assistant",
            "🔍 Document-Form Validation",
            "🌳 Decision Tree Classifier",
            "🔮 Performance Prediction (Logistic Regression)",
            "💾 Data Management",
            "📄 PDF Reports",
            "🌐 API Integration",
            "⚙️ System Settings"
        ]
    )
    
    # Route to selected module
    if app_mode == "📊 Performance Dashboard":
        create_performance_dashboard(analyzer)
    
    elif app_mode == "📋 Document Analysis":
        create_document_analysis_module(analyzer)
    
    elif app_mode == "🤖 Intelligence Hub":
        create_institutional_intelligence_hub(analyzer)
    
    elif app_mode == "🔍 RAG Data Management":
        create_rag_dashboard(analyzer)
    
    elif app_mode == "📋 NAAC Accreditation Assistant":
        # NAAC Module Implementation
        st.title("🏛️ NAAC Accreditation Assistant")
        st.markdown("""
        <div style='background-color: #e8f4fd; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
        <h4>🎯 Welcome to NAAC Accreditation Assistant</h4>
        <p>This comprehensive tool helps you prepare for NAAC accreditation by:</p>
        <ul>
            <li>📝 Guiding you through all 7 criteria with interactive forms</li>
            <li>📊 Calculating your estimated CGPA and grade based on NAAC weightages</li>
            <li>🔍 Identifying gaps in your documentation and data submission</li>
            <li>📑 Generating a draft Self-Study Report (SSR) for review</li>
        </ul>
        <p><strong>Total Weightage:</strong> 1000 marks | <strong>Target Grade:</strong> A+ (3.26 CGPA)</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Initialize session state for NAAC data
        if 'naac_responses' not in st.session_state:
            st.session_state.naac_responses = {}
        if 'naac_institution_name' not in st.session_state:
            st.session_state.naac_institution_name = st.session_state.get('institution_name', 'Your Institution')
        
        # Sidebar navigation for NAAC module
        st.sidebar.markdown("---")
        st.sidebar.subheader("📋 NAAC Navigation")
        
        naac_tab = st.sidebar.radio(
            "Select NAAC Function:",
            ["📝 Data Entry", "📊 Gap Analysis", "📄 Score Report", "📑 SSR Generator"]
        )
        
        if naac_tab == "📝 Data Entry":
            st.header("📝 NAAC Data Entry")
            st.markdown("Enter data for each criterion as per NAAC requirements")
            
            criterion = st.sidebar.selectbox(
                "Select Criterion to work on:",
                [f"Criterion {i}" for i in range(1, 8)],
                format_func=lambda x: {
                    "Criterion 1": "Criterion 1: Curricular Aspects (150 marks)",
                    "Criterion 2": "Criterion 2: Teaching-Learning and Evaluation (200 marks)",
                    "Criterion 3": "Criterion 3: Research, Innovations and Extension (250 marks)",
                    "Criterion 4": "Criterion 4: Infrastructure and Learning Resources (100 marks)",
                    "Criterion 5": "Criterion 5: Student Support and Progression (100 marks)",
                    "Criterion 6": "Criterion 6: Governance, Leadership and Management (100 marks)",
                    "Criterion 7": "Criterion 7: Institutional Values and Best Practices (100 marks)"
                }.get(x, x)
            )
            criterion_num = int(criterion.split()[1])
            
            # Create form for selected criterion
            new_responses = create_criteria_forms(analyzer, criterion_num, st.session_state.naac_responses)
            
            # Save button
            col1, col2, col3 = st.columns([1, 1, 3])
            with col1:
                if st.button("💾 Save Criterion Data", type="primary"):
                    st.session_state.naac_responses.update(new_responses)
                    st.success(f"✅ Criterion {criterion_num} data saved successfully!")
            
            with col2:
                if st.button("🔄 Reset Criterion", type="secondary"):
                    for key in list(st.session_state.naac_responses.keys()):
                        if key.startswith(str(criterion_num)):
                            del st.session_state.naac_responses[key]
                    st.success(f"✅ Criterion {criterion_num} data reset!")
                    st.rerun()
            
            # Show completion status
            st.sidebar.markdown("---")
            st.sidebar.subheader("📊 Overall Progress")
            completed = sum(1 for r in st.session_state.naac_responses.values() if r.get('response'))
            total = len(METRICS)
            st.sidebar.progress(completed/total if total > 0 else 0)
            st.sidebar.write(f"**{completed}/{total} metrics completed**")
            st.sidebar.write(f"**Completion:** {(completed/total*100):.1f}%")
        
        elif naac_tab == "📊 Gap Analysis":
            create_gap_analysis(analyzer, {'metric_responses': st.session_state.naac_responses})
        
        elif naac_tab == "📄 Score Report":
            scoring_engine = NAACScoringEngine()
            
            # Calculate scores
            cgpa = scoring_engine.calculate_cgpa(st.session_state.naac_responses)
            grade = scoring_engine.get_grade(cgpa)
            criterion_scores = scoring_engine.calculate_criterion_score(st.session_state.naac_responses)
            
            # Display score report
            st.header("🎯 NAAC Score Report")
            
            # Metrics Cards
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Estimated CGPA", f"{cgpa:.2f}/4.00", 
                         delta=f"Target: 3.26", delta_color="normal")
            with col2:
                st.metric("Projected Grade", grade, 
                         delta="A+ target", delta_color="off")
            with col3:
                total_score = cgpa * 250
                st.metric("Total Score", f"{total_score:.0f}/1000", 
                         delta="A+ needs 815+", delta_color="off")
            with col4:
                completed = sum(1 for r in st.session_state.naac_responses.values() if r.get('response'))
                total = len(METRICS)
                st.metric("Completion", f"{completed}/{total}", 
                         delta=f"{(completed/total*100):.1f}%", delta_color="normal")
            
            st.markdown("---")
            
            # Criterion-wise scores
            st.subheader("📊 Criterion-wise Performance")
            
            for criterion in range(1, 8):
                score = criterion_scores.get(criterion, 0)
                weight = CRITERION_WEIGHTAGES[criterion]
                weighted_score = score * weight
                
                col1, col2, col3 = st.columns([2, 3, 1])
                with col1:
                    st.write(f"**Criterion {criterion}**")
                with col2:
                    st.progress(score/4, text=f"Score: {score:.2f}/4.00")
                with col3:
                    st.write(f"**{weighted_score:.0f}/{weight}**")
            
            st.markdown("---")
            
            # Recommendations
            st.subheader("💡 Recommendations for Improvement")
            
            if cgpa < 2.0:
                st.error("⚠️ Your estimated CGPA is below B grade. Immediate action required!")
                st.markdown("""
                **Priority Actions:**
                1. Complete all missing metrics
                2. Verify data accuracy with supporting documents
                3. Focus on high-weightage criteria (Criterion 3 - 250 marks)
                4. Ensure proper documentation with geo-tagging where required
                """)
            elif cgpa < 3.0:
                st.warning("📊 Your estimated CGPA is below A grade. Focus on improvement areas.")
                weak_criteria = [c for c in range(1, 8) if criterion_scores.get(c, 0) < 2.5]
                if weak_criteria:
                    st.write(f"**Focus on Criteria:** {', '.join([f'Criterion {c}' for c in weak_criteria])}")
            else:
                st.success("✅ Great progress! Continue to complete all metrics and validate your data.")
                st.markdown("**Next Steps:**")
                st.markdown("""
                - Complete any remaining metrics
                - Prepare supporting documents
                - Conduct mock peer team visit
                - Generate and review SSR
                """)
        
        elif naac_tab == "📑 SSR Generator":
            generate_ssr(analyzer, {
                'metric_responses': st.session_state.naac_responses,
                'institution_name': st.session_state.naac_institution_name,
                'cycle': st.session_state.get('cycle', 1)
            })
    
    elif app_mode == "🔍 Document-Form Validation":
        create_rag_validation_dashboard(analyzer)
    
    elif app_mode == "🌳 Decision Tree Classifier":
        create_decision_tree_module(analyzer)
    
    elif app_mode == "🔮 Performance Prediction (Logistic Regression)":
        predict_performance_tab(analyzer)
    
    elif app_mode == "💾 Data Management":
        create_data_management_module(analyzer)
    
    elif app_mode == "📄 PDF Reports":
        create_pdf_report_module(analyzer)
    
    elif app_mode == "🌐 API Integration":
        create_api_documentation()
    
    elif app_mode == "⚙️ System Settings":
        create_system_settings(analyzer)
    
    # Footer
    st.markdown("---")
    st.markdown(f"""
    <div style='text-align: center; color: #6c757d;'>
    <p><strong>UGC/AICTE Institutional Analytics Platform</strong> | AI-Powered Decision Support System</p>
    <p>Version 2.0 | For authorized use only | NAAC Accreditation Assistant | Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# RUN APPLICATION
# ============================================================================
if __name__ == "__main__":
    main()
# NAAC Accreditation Assistant - Complete with Document Upload
import streamlit as st
import sys
import os
import json
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.naac_config import (
    CRITERIA, TOTAL_WEIGHTAGE, ORIENTATION_CATEGORIES, 
    LEGACY_CATEGORIES, METRICS
)
from modules.database import get_db
from modules.enhanced_criteria_forms import create_enhanced_criteria_forms

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
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    .binary-accredited { background: #28a745; color: white; padding: 0.5rem; border-radius: 5px; text-align: center; }
    .binary-awaiting { background: #ffc107; color: #333; padding: 0.5rem; border-radius: 5px; text-align: center; }
    .binary-not { background: #dc3545; color: white; padding: 0.5rem; border-radius: 5px; text-align: center; }
    .metric-card { background: #f8f9fa; padding: 1rem; border-radius: 10px; margin-bottom: 1rem; border-left: 4px solid #1e3a5f; }
    .stProgress > div > div > div > div { background-color: #1e3a5f; }
</style>
""", unsafe_allow_html=True)

# Initialize database
db = get_db()

# Session state
if 'institution_id' not in st.session_state:
    st.session_state.institution_id = None
if 'application_id' not in st.session_state:
    st.session_state.application_id = None
if 'active_step' not in st.session_state:
    st.session_state.active_step = 0
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'institution_profile' not in st.session_state:
    st.session_state.institution_profile = {}
if 'naac_responses' not in st.session_state:
    st.session_state.naac_responses = {}

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.markdown("### 🎓 NAAC Assistant")
    st.markdown("---")
    
    if not st.session_state.logged_in:
        st.subheader("🔐 Login / Register")
        
        with st.form("login_form"):
            aishe_code = st.text_input("AISHE Code", placeholder="Enter your institution AISHE code")
            submitted = st.form_submit_button("Login / Register")
            
            if submitted and aishe_code:
                institution = db.get_institution(aishe_code)
                
                if institution:
                    st.session_state.institution_profile = institution
                    st.session_state.institution_id = institution['id']
                    st.session_state.logged_in = True
                    
                    application = db.get_active_application(institution['id'])
                    if application:
                        st.session_state.application_id = application['id']
                        responses = db.get_metric_responses(application['id'])
                        st.session_state.naac_responses = responses
                    else:
                        app_id = db.create_application(institution['id'])
                        st.session_state.application_id = app_id
                        st.session_state.naac_responses = {}
                    
                    st.success(f"Welcome back, {institution['institution_name']}!")
                    st.rerun()
                else:
                    st.session_state.temp_aishe = aishe_code
                    st.info("New institution. Please complete your profile below.")
        
        if 'temp_aishe' in st.session_state:
            st.subheader("📝 Complete Profile")
            with st.form("new_institution_form"):
                inst_name = st.text_input("Institution Name *")
                inst_type = st.selectbox("Type of University *",
                                        ["Central University", "State University", "Private University", 
                                         "Deemed to be University", "Institution of National Importance"])
                orientation = st.selectbox("Orientation Category *", list(ORIENTATION_CATEGORIES.values()))
                legacy = st.selectbox("Legacy Category *", list(LEGACY_CATEGORIES.values()))
                city = st.text_input("City")
                state = st.text_input("State")
                website = st.text_input("Website")
                
                submitted_profile = st.form_submit_button("Save Profile")
                
                if submitted_profile:
                    profile_data = {
                        'name': inst_name,
                        'aishe_code': st.session_state.temp_aishe,
                        'type': inst_type,
                        'orientation_category': orientation,
                        'legacy_category': legacy,
                        'city': city,
                        'state': state,
                        'website': website
                    }
                    institution_id = db.save_institution(profile_data)
                    institution = db.get_institution(st.session_state.temp_aishe)
                    
                    st.session_state.institution_profile = institution
                    st.session_state.institution_id = institution_id
                    st.session_state.logged_in = True
                    
                    app_id = db.create_application(institution_id)
                    st.session_state.application_id = app_id
                    st.session_state.naac_responses = {}
                    
                    del st.session_state.temp_aishe
                    st.success("Profile created! Welcome!")
                    st.rerun()
    
    else:
        st.success(f"👤 {st.session_state.institution_profile.get('institution_name', 'User')}")
        st.caption(f"AISHE: {st.session_state.institution_profile.get('aishe_code', '')}")
        
        st.markdown("---")
        
        total_completed = sum(1 for r in st.session_state.naac_responses.values() if r.get('response') and r.get('response') != '')
        total_metrics = len(METRICS)
        if total_metrics > 0:
            progress_pct = (total_completed / total_metrics) * 100
            st.progress(progress_pct / 100)
            st.caption(f"Progress: {progress_pct:.1f}% ({total_completed}/{total_metrics})")
        
        st.markdown("---")
        
        steps = [
            {"name": "📊 Profile", "step": 0},
            {"name": "📚 Curriculum", "step": 1},
            {"name": "👨‍🏫 Faculty", "step": 2},
            {"name": "📖 Teaching", "step": 3},
            {"name": "🔬 Research", "step": 4},
            {"name": "🎭 EC/CC", "step": 5},
            {"name": "🤝 Community", "step": 6},
            {"name": "🌿 Green", "step": 7},
            {"name": "⚙️ Governance", "step": 8},
            {"name": "🏗️ Infra", "step": 9},
            {"name": "💰 Finance", "step": 10},
            {"name": "📊 Report", "step": 11}
        ]
        
        for step in steps:
            if st.button(step["name"], key=f"nav_{step['step']}", use_container_width=True):
                st.session_state.active_step = step["step"]
                st.rerun()
        
        st.markdown("---")
        if st.button("🚪 Logout", use_container_width=True):
            for key in ['logged_in', 'institution_id', 'application_id', 'institution_profile', 'naac_responses']:
                st.session_state[key] = {} if key in ['institution_profile', 'naac_responses'] else None if key not in ['logged_in'] else False
            st.session_state.active_step = 0
            st.rerun()

# ============================================================================
# MAIN CONTENT
# ============================================================================

st.markdown('<div class="main-header">', unsafe_allow_html=True)
st.title("🏛️ NAAC Accreditation Assistant")
st.markdown("### Based on Dr. Radhakrishnan Committee Report (Nov 2023)")
st.markdown("#### Upload documents, enter data, track progress")
st.markdown('</div>', unsafe_allow_html=True)

if not st.session_state.logged_in:
    st.info("👈 Please login or register using your AISHE code to continue.")
else:
    active_step = st.session_state.active_step
    
    if active_step == 0:
        st.header("🏛️ Institution Profile")
        
        col1, col2 = st.columns(2)
        with col1:
            inst_name = st.text_input("Institution Name *", value=st.session_state.institution_profile.get('institution_name', ''))
            inst_type = st.selectbox("Type of University *",
                                    ["Central University", "State University", "Private University", 
                                     "Deemed to be University", "Institution of National Importance"],
                                    index=["Central University", "State University", "Private University", 
                                           "Deemed to be University", "Institution of National Importance"].index(
                                               st.session_state.institution_profile.get('institution_type', 'Central University')) if st.session_state.institution_profile.get('institution_type') else 0)
            orientation = st.selectbox("Orientation Category *", list(ORIENTATION_CATEGORIES.values()))
            legacy = st.selectbox("Legacy Category *", list(LEGACY_CATEGORIES.values()))
        
        with col2:
            city = st.text_input("City", value=st.session_state.institution_profile.get('city', ''))
            state = st.text_input("State", value=st.session_state.institution_profile.get('state', ''))
            website = st.text_input("Website", value=st.session_state.institution_profile.get('website', ''))
        
        if st.button("💾 Save Profile", type="primary"):
            profile_data = {
                'name': inst_name,
                'aishe_code': st.session_state.institution_profile.get('aishe_code'),
                'type': inst_type,
                'orientation_category': orientation,
                'legacy_category': legacy,
                'city': city,
                'state': state,
                'website': website
            }
            db.save_institution(profile_data)
            st.session_state.institution_profile = db.get_institution(st.session_state.institution_profile.get('aishe_code'))
            st.success("✅ Profile saved!")
            st.rerun()
    
    elif 1 <= active_step <= 10:
        criterion_num = active_step
        
        # Create enhanced forms with document upload
        new_responses = create_enhanced_criteria_forms(
            None, 
            criterion_num, 
            st.session_state.naac_responses,
            st.session_state.application_id,
            db
        )
        
        if st.button(f"💾 Save Criterion {criterion_num}", type="primary"):
            for metric_code, response_data in new_responses.items():
                db.save_metric_response(st.session_state.application_id, metric_code, response_data)
            st.session_state.naac_responses.update(new_responses)
            st.success(f"✅ Criterion {criterion_num} saved with documents!")
            st.rerun()
    
    elif active_step == 11:
        st.header("📊 Report & Score")
        
        total_completed = sum(1 for r in st.session_state.naac_responses.values() if r.get('response') and r.get('response') != '')
        total_metrics = len(METRICS)
        completion_pct = (total_completed / total_metrics * 100) if total_metrics > 0 else 0
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Metrics Completed", f"{total_completed}/{total_metrics}")
        with col2:
            st.metric("Completion Rate", f"{completion_pct:.1f}%")
        with col3:
            if completion_pct >= 60:
                st.markdown('<div class="binary-accredited">ACCREDITED</div>', unsafe_allow_html=True)
            elif completion_pct >= 50:
                st.markdown('<div class="binary-awaiting">AWAITING ACCREDITATION</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="binary-not">NOT ACCREDITED</div>', unsafe_allow_html=True)
        
        st.subheader("📊 Criterion-wise Progress")
        for criterion_num in range(1, 11):
            criterion_metrics = {k: v for k, v in METRICS.items() if k.startswith(f'{criterion_num}.')}
            if criterion_metrics:
                completed = sum(1 for code in criterion_metrics.keys() 
                              if code in st.session_state.naac_responses and st.session_state.naac_responses[code].get('response') and st.session_state.naac_responses[code].get('response') != '')
                pct = (completed / len(criterion_metrics)) * 100
                st.write(f"**Criterion {criterion_num}: {CRITERIA[criterion_num]['name']}**")
                st.progress(pct/100, text=f"{pct:.0f}% completed")
        
        st.subheader("📑 Export Data")
        if st.button("Export Report", type="primary"):
            export_data = {
                'institution': st.session_state.institution_profile,
                'responses': st.session_state.naac_responses,
                'exported_at': datetime.now().isoformat()
            }
            json_str = json.dumps(export_data, indent=2, default=str)
            st.download_button("Download JSON", json_str, f"naac_report_{datetime.now().strftime('%Y%m%d')}.json", "application/json")
            st.success("Report exported!")

st.markdown("---")
st.caption("NAAC Accreditation Assistant | Based on Dr. Radhakrishnan Committee Report (Nov 2023)")

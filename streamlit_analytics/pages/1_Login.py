import sys
import os
import streamlit as st

# Add root directory to path to import core and modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.analyzer import InstitutionalAIAnalyzer
from institution.auth import create_institution_login

st.set_page_config(
    page_title="SUGAM Portal Login", 
    layout="wide",
)

# Initialize session state for users if not present
if 'institution_user' not in st.session_state:
    st.session_state.institution_user = None
if 'ugc_aicte_user' not in st.session_state:
    st.session_state.ugc_aicte_user = None
if 'user_role' not in st.session_state:
    st.session_state.user_role = None

try:
    analyzer = InstitutionalAIAnalyzer()
    
    # Check if already logged in
    if st.session_state.institution_user or st.session_state.ugc_aicte_user:
        user_name = st.session_state.institution_user['contact_person'] if st.session_state.institution_user else st.session_state.ugc_aicte_user
        st.success(f"Logged in as {user_name} ({st.session_state.user_role})")
        if st.button("Logout"):
            st.session_state.institution_user = None
            st.session_state.ugc_aicte_user = None
            st.session_state.user_role = None
            st.rerun()
    else:
        # Show actual login from institution/auth.py
        create_institution_login(analyzer)
        
        # Add UGC/AICTE Login as a toggle or separate section if needed
        with st.expander("🔐 UGC / AICTE Admin Login"):
            ugc_user = st.text_input("Admin Username", key="ugc_username")
            ugc_pass = st.text_input("Admin Password", type="password", key="ugc_password")
            if st.button("Login as Admin"):
                if ugc_user == "admin" and ugc_pass == "admin123":
                    st.session_state.ugc_aicte_user = "UGC Admin"
                    st.session_state.user_role = "UGC/AICTE"
                    st.success("Admin Login Successful!")
                    st.rerun()
                else:
                    st.error("Invalid Admin Credentials")

except Exception as e:
    st.error(f"Error in Portal Login: {str(e)}")

st.markdown("---")
st.caption("✨ AES-256 Government Grade Encryption Active")

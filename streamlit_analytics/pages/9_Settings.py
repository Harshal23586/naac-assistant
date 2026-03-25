import sys
import os
import streamlit as st

# Add root directory to path to import core and modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.analyzer import InstitutionalAIAnalyzer
from modules.system_settings import create_system_settings

st.set_page_config(
    page_title="SUGAM System Settings", 
    layout="wide"
)

try:
    analyzer = InstitutionalAIAnalyzer()
    create_system_settings(analyzer)
except Exception as e:
    st.error(f"Error initializing System Settings: {str(e)}")

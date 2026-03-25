import sys
import os
import streamlit as st

# Add root directory to path to import core and modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.analyzer import InstitutionalAIAnalyzer
from modules.intelligence_hub import create_institutional_intelligence_hub

st.set_page_config(
    page_title="SUGAM Institutional Intelligence Hub", 
    layout="wide"
)

try:
    analyzer = InstitutionalAIAnalyzer()
    create_institutional_intelligence_hub(analyzer)
except Exception as e:
    st.error(f"Error initializing Intelligence Hub: {str(e)}")

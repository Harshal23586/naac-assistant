import sys
import os
import streamlit as st

# Add root directory to path to import core and modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.analyzer import InstitutionalAIAnalyzer
from modules.pdf_reports import create_pdf_report_module

try:
    analyzer = InstitutionalAIAnalyzer()
    create_pdf_report_module(analyzer)
except Exception as e:
    st.error(f"Error initializing Report Generation: {str(e)}")


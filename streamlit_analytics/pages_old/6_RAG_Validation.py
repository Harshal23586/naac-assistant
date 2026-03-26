import sys
import os
import streamlit as st

# Add root directory to path to import core and modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.analyzer import InstitutionalAIAnalyzer
from modules.rag_dashboard import create_rag_dashboard
try:
    from modules.rag_core import create_rag_validation_dashboard
except ImportError:
    # Fallback if not in rag_core
    from modules.rag_dashboard import create_rag_validation_dashboard

try:
    analyzer = InstitutionalAIAnalyzer()
    
    tabs = st.tabs(["RAG Dashboard", "RAG Validation"])
    
    with tabs[0]:
        create_rag_dashboard(analyzer)
    
    with tabs[1]:
        create_rag_validation_dashboard(analyzer)
        
except Exception as e:
    st.error(f"Error initializing RAG Validation: {str(e)}")


import sys
import os
import streamlit as st

# Embed Core Paths explicitly securing physical modules flawlessly seamlessly natively mathematically appropriately cleanly
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.analyzer import InstitutionalAIAnalyzer
from modules.dashboard import create_performance_dashboard

# Strip Sidebar interactions generating pure analytical canvases mapping cleanly smoothly natively effortlessly
# Render Global Analytics natively gracefully seamlessly smoothly
try:
    analyzer = InstitutionalAIAnalyzer()
    create_performance_dashboard(analyzer)
except Exception as e:
    st.error(f"Critical Backend Matrix Offline: {str(e)}")


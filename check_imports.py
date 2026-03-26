# Quick check of enhanced forms
import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from modules.enhanced_criteria_forms import create_criteria_forms_with_guidance
    print("✅ Enhanced forms imported successfully")
except Exception as e:
    print(f"❌ Enhanced forms import failed: {e}")
    
try:
    from modules.metric_guidance import METRIC_GUIDANCE
    print(f"✅ Metric guidance loaded: {len(METRIC_GUIDANCE)} metrics")
except Exception as e:
    print(f"❌ Metric guidance load failed: {e}")
    
print("\nChecking metric guidance keys:")
if 'METRIC_GUIDANCE' in dir():
    print(f"  Keys: {list(METRIC_GUIDANCE.keys())[:5]}...")

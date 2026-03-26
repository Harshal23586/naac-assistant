# test_imports.py
import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print(f"Current file: {__file__}")
print(f"Python path: {sys.path}")

try:
    from config.naac_config import CRITERIA
    print("✅ config.naac_config imported successfully!")
    print(f"Found {len(CRITERIA)} criteria")
except Exception as e:
    print(f"❌ Error importing config: {e}")
    
try:
    from modules.enhanced_criteria_forms import create_criteria_forms_with_guidance
    print("✅ modules.enhanced_criteria_forms imported successfully!")
except Exception as e:
    print(f"❌ Error importing modules: {e}")

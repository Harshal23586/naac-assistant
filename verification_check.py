# verification_check.py
import streamlit as st
import pandas as pd
import sqlite3
import os

def verify_system():
    """Verify all system components"""
    
    print("🔍 SUGAM System Verification")
    print("=" * 50)
    
    # Check 1: File structure
    print("\n📁 FILE STRUCTURE:")
    required_files = [
        'main.py',
        'requirements.txt',
        'institution/__init__.py',
        'institution/auth.py',
        'institution/dashboard.py',
        'institution/forms.py',
        'institution/documents.py',
        'institution/submissions.py',
        'core/__init__.py',
        'core/analyzer.py'
    ]
    
    for file in required_files:
        exists = os.path.exists(file)
        print(f"  {'✅' if exists else '❌'} {file}")
    
    # Check 2: Database
    print("\n🗄️ DATABASE:")
    try:
        conn = sqlite3.connect('institutions.db')
        cursor = conn.cursor()
        
        # Check tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        
        required_tables = ['institutions', 'institution_users', 
                          'institution_documents', 'institution_submissions']
        
        for table in required_tables:
            exists = table in tables
            print(f"  {'✅' if exists else '❌'} Table: {table}")
        
        conn.close()
    except Exception as e:
        print(f"  ❌ Database error: {e}")
    
    # Check 3: Analyzer methods
    print("\n🤖 ANALYZER METHODS:")
    from core.analyzer import InstitutionalAIAnalyzer
    
    analyzer = InstitutionalAIAnalyzer()
    
    required_methods = [
        'authenticate_institution_user',
        'create_institution_user',
        'save_institution_submission',
        'get_institution_submissions',
        'save_uploaded_documents',
        'get_institution_documents',
        'calculate_performance_score',
        'generate_approval_recommendation',
        'assess_risk_level'
    ]
    
    for method in required_methods:
        exists = hasattr(analyzer, method) and callable(getattr(analyzer, method))
        print(f"  {'✅' if exists else '❌'} Method: {method}()")
    
    # Check 4: Data generation
    print("\n📊 DATA GENERATION:")
    try:
        df = analyzer.historical_data
        institutions = df['institution_id'].nunique()
        years = df['year'].nunique()
        print(f"  ✅ Data: {institutions} institutions × {years} years")
        print(f"  ✅ Records: {len(df)} total")
    except Exception as e:
        print(f"  ❌ Data error: {e}")
    
    print("\n" + "=" * 50)
    print("🔍 Verification Complete")

if __name__ == "__main__":
    verify_system()


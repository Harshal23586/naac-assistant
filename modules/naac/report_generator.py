import streamlit as st
import pandas as pd
from datetime import datetime

def generate_ssr(analyzer, application_data):
    st.header("Self-Study Report Generator")
    
    responses = application_data.get('metric_responses', {})
    institution_name = application_data.get('institution_name', 'Your Institution')
    
    completed = len([r for r in responses.values() if r.get('response')])
    total = 78
    
    st.subheader("Executive Summary")
    st.write(f"Institution: {institution_name}")
    st.write(f"Date: {datetime.now().strftime('%B %d, %Y')}")
    st.write(f"Progress: {completed}/{total} metrics completed")
    
    st.subheader("Next Steps")
    st.write("1. Complete all 7 criteria data entry")
    st.write("2. Upload supporting documents")
    st.write("3. Review and validate data")
    st.write("4. Generate final SSR")
    
    if st.button("Download Report"):
        data = []
        for code, val in responses.items():
            data.append({'Metric': code, 'Response': str(val.get('response', ''))[:200]})
        df = pd.DataFrame(data)
        csv = df.to_csv(index=False)
        st.download_button("Download CSV", csv, f"ssr_{datetime.now().strftime('%Y%m%d')}.csv")

import streamlit as st
import pandas as pd

def create_gap_analysis(analyzer, institution_data):
    st.header("NAAC Gap Analysis")
    
    responses = institution_data.get('metric_responses', {})
    completed = len([r for r in responses.values() if r.get('response')])
    total = 78
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Completed Metrics", f"{completed}/{total}")
    with col2:
        st.metric("Completion Rate", f"{(completed/total*100):.1f}%")
    with col3:
        st.metric("Remaining", f"{total - completed}")
    
    st.progress(completed/total)
    
    st.subheader("Missing Metrics")
    missing = []
    for code in ['1.1.1', '1.1.2', '1.1.3', '2.1.1', '2.2.2', '3.1.2', '4.3.3', '5.2.2']:
        if code not in responses or not responses[code].get('response'):
            missing.append(code)
    
    if missing:
        for m in missing:
            st.write(f"- {m}")
    else:
        st.success("All key metrics completed!")
    
    return pd.DataFrame()

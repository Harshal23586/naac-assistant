import streamlit as st

st.set_page_config(
    page_title="SUGAM Institutional Intelligence", 
    layout="wide",
)

st.markdown(
    """
    <div style='text-align: center; padding-top: 50px;'>
        <h3 style='color: #3b82f6;'>🛡️ NEP 2020 Compliant Platform</h3>
        <h1 style='font-size: 5rem; font-weight: 800; margin-bottom: 0px;'>The Future of</h1>
        <h1 style='font-size: 5rem; font-weight: 800; color: #3b82f6; margin-top: 0px;'>Institutional Intelligence</h1>
        <p style='font-size: 1.2rem; color: #94a3b8; max-width: 800px; margin: 0 auto; margin-top: 20px;'>
            Leverage deep machine learning and explicit statutory policy engines to instantly verify, evaluate, and approve educational institutions securely.
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.subheader("🔬 Predictive Risk")
        st.markdown("Live Decision Tree ML identifies high-risk applications dynamically.")

with col2:
    with st.container(border=True):
        st.subheader("🛡️ Statutory Checks")
        st.markdown("Rigorous and enforceable rules protecting UGC & AICTE standards.")

with col3:
    with st.container(border=True):
        st.subheader("📈 Aesthetic Insights")
        st.markdown("Beautiful, robust dashboards mapped flawlessly with analytics.")

st.info("👈 Navigate to Login, Predictor, or Analytics using the sidebar.")

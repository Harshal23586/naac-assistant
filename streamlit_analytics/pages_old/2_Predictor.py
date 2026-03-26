import sys
import os
import streamlit as st
import requests

# Embed Core Paths explicitly securing physical modules flawlessly seamlessly natively mathematically appropriately cleanly
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

st.title("🔬 Application Metrics & Prediction Simulator")
st.markdown("Adjust parameters to simulate live ML predictions. Streams real-time insights from the FastAPI microservice.")

col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.subheader("Institution Parameters")
        sfr = st.number_input("Student-Faculty Ratio", value=15.0, step=0.1)
        score = st.number_input("Performance Score (0-10)", value=6.5, step=0.1)
        finance = st.number_input("Financial Stability (0-10)", value=7.0, step=0.1)
        phd = st.number_input("PhD Faculty Ratio (0.0 - 1.0)", value=0.5, step=0.05)
        
        predict_btn = st.button("Run AI Prediction Engine", use_container_width=True, type="primary")

with col2:
    if predict_btn:
        payload = {
            "student_faculty_ratio": sfr,
            "phd_faculty_ratio": phd,
            "performance_score": score,
            "financial_stability_score": finance,
            "research_publications": 20,
            "research_grants_amount": 1000000.0,
            "industry_collaborations": 5,
            "placement_rate": 75.0,
            "compliance_score": 7.0,
            "patents_filed": 2,
            "digital_infrastructure_score": 6.0,
            "library_volumes": 15000,
            "laboratory_equipment_score": 7.0,
            "administrative_efficiency": 6.5,
            "higher_education_rate": 20.0,
            "entrepreneurship_cell_score": 6.0,
            "community_projects": 5,
            "rural_outreach_score": 6.0,
            "inclusive_education_index": 6.5
        }
        
        with st.spinner("Analyzing Models..."):
            try:
                # 1. ML Prediction
                ml_res = requests.post("http://localhost:8002/api/v1/predict/risk", json=payload)
                if ml_res.ok:
                    ml_data = ml_res.json().get("data", {})
                    st.success("Decision Tree Inference Complete")
                    
                    risk = ml_data.get("predicted_risk", "")
                    conf = ml_data.get("confidence", 0) * 100
                    
                    if "Critical" in risk or "High" in risk:
                        st.error(f"**{risk}** (Confidence: {conf:.1f}%)")
                    else:
                        st.info(f"**{risk}** (Confidence: {conf:.1f}%)")
                else:
                    st.error("ML Engine returned an error. Ensure model is trained via Port 8002.")
                
                # 2. Policy Engine
                pol_res = requests.post("http://localhost:8002/api/v1/policy/evaluate", json=payload)
                if pol_res.ok:
                    pol_data = pol_res.json().get("data", {})
                    st.subheader("Statutory Policy Check (UGC/AICTE)")
                    evals = pol_data.get("evaluations", [])
                    
                    for rule in evals:
                        if rule["status"] == "COMPLIANT":
                            st.success(f"**{rule['policy']}**: {rule['domain']} ({rule['actual']})")
                        elif rule["status"] == "WARNING":
                            st.warning(f"**{rule['policy']}**: {rule['domain']} ({rule['actual']})")
                        else:
                            st.error(f"**{rule['policy']}**: {rule['domain']} ({rule['actual']})\n\nRequirement: {rule['requirement']}")
                            
                    if pol_data.get("is_approval_blocked_by_statute", False):
                        st.error("🚨 Statutory Rejection Override Applied: Regardless of ML Risk, this physical breach halts approval.")
                
            except Exception as e:
                st.exception(e)
    else:
        st.info("Awaiting Inference Data. Modify metrics and click predict.")



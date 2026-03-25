# modules/quick_predictor.py
import streamlit as st
import pandas as pd
from modules.decision_tree_classifier import InstitutionalDecisionTreeClassifier

def create_quick_predictor(analyzer):
    """Create a quick risk prediction interface"""
    
    st.title("⚡ Quick Risk Predictor")
    st.markdown("Predict risk level for an institution in seconds")
    
    # Initialize classifier
    classifier = InstitutionalDecisionTreeClassifier(analyzer)
    
    # Try to load model
    if not classifier.load_model():
        st.warning("No trained model found. Please train a model first in the Decision Tree module.")
        return
    
    # Simplified input form
    col1, col2 = st.columns(2)
    
    with col1:
        student_faculty_ratio = st.slider("Student-Faculty Ratio", 5.0, 40.0, 15.0, 0.5)
        phd_faculty_ratio = st.slider("PhD Faculty Ratio", 0.1, 1.0, 0.5, 0.05)
        placement_rate = st.slider("Placement Rate (%)", 40.0, 100.0, 75.0, 1.0)
        performance_score = st.slider("Performance Score", 1.0, 10.0, 5.5, 0.1)
    
    with col2:
        research_publications = st.number_input("Research Publications", 0, 100, 20)
        research_grants = st.number_input("Research Grants (₹ Lakhs)", 0, 10000, 1000)
        industry_collabs = st.number_input("Industry Collaborations", 0, 20, 5)
        compliance_score = st.slider("Compliance Score", 1.0, 10.0, 7.0, 0.1)
    
    # Prepare input data
    input_data = {
        'student_faculty_ratio': student_faculty_ratio,
        'phd_faculty_ratio': phd_faculty_ratio,
        'research_publications': research_publications,
        'research_grants_amount': research_grants * 100000,  # Convert to actual amount
        'industry_collaborations': industry_collabs,
        'placement_rate': placement_rate,
        'compliance_score': compliance_score,
        'performance_score': performance_score,
        # Add default values for other required features
        'patents_filed': 2,
        'digital_infrastructure_score': 6.0,
        'library_volumes': 15000,
        'laboratory_equipment_score': 7.0,
        'financial_stability_score': 7.0,
        'administrative_efficiency': 6.5,
        'higher_education_rate': 20.0,
        'entrepreneurship_cell_score': 6.0,
        'community_projects': 5,
        'rural_outreach_score': 6.0,
        'inclusive_education_index': 6.5
    }
    
    if st.button("🔮 Predict Risk", type="primary", use_container_width=True):
        with st.spinner("Analyzing..."):
            prediction = classifier.predict_risk(input_data)
            
            if prediction:
                # Display result
                risk_level = prediction['predicted_risk']
                confidence = prediction['confidence']
                
                # Color code based on risk
                if 'Critical' in risk_level:
                    color = 'red'
                    icon = '🔴'
                    recommendation = "Immediate improvements required"
                elif 'High' in risk_level:
                    color = 'orange'
                    icon = '🟠'
                    recommendation = "Close monitoring needed"
                elif 'Medium' in risk_level:
                    color = 'yellow'
                    icon = '🟡'
                    recommendation = "Moderate risk, regular monitoring"
                else:
                    color = 'green'
                    icon = '🟢'
                    recommendation = "Low risk, good performance"
                
                st.markdown(f"""
                <div style='padding: 20px; background-color: #f8f9fa; border-radius: 10px; border: 2px solid {color};'>
                <h2 style='color: {color};'>{icon} Predicted Risk: {risk_level}</h2>
                <p><strong>Confidence:</strong> {confidence:.1%}</p>
                <p><strong>Recommendation:</strong> {recommendation}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # --- NEW ML-DRIVEN APPROVAL LOGIC ---
                from core.database import generate_approval_recommendation
                from utils.helpers import generate_decision_support_report
                
                ml_approval_rec = generate_approval_recommendation(performance_score, risk_level, doc_verification=True, metrics_dict=input_data)
                decision_report_dict = generate_decision_support_report(performance_score, risk_level, metrics_dict=input_data)
                
                report_md = "\n".join([f"- {r}" for r in decision_report_dict['reasons']])
                policy_md = "\n".join([f"- {p}" for p in decision_report_dict['policy_alignments']])
                decision_report = f"**Reasons:**\n{report_md}\n\n**Policy Alignments:**\n{policy_md}"
                
                st.markdown("---")
                st.subheader("🏛️ AI/ML-Driven Approval Decision")
                st.info("This approval recommendation is directly enforced by the Live Decision Tree Machine Learning Model.")
                
                if "Rejection" in ml_approval_rec or "Critical" in risk_level:
                    st.error(f"**Final Verdict**: {ml_approval_rec}")
                elif "Monitoring" in ml_approval_rec or "Conditional" in ml_approval_rec:
                    st.warning(f"**Final Verdict**: {ml_approval_rec}")
                else:
                    st.success(f"**Final Verdict**: {ml_approval_rec}")
                    
                with st.expander("View Policy-Aware Decision Support Report", expanded=True):
                    st.markdown(decision_report)
                    
                # --- NEW POLICY ENGINE VISUALIZATION ---
                from core.policy_engine import StatutoryPolicyEngine
                st.subheader("⚖️ Statutory Policy Compliance")
                compliance_results = StatutoryPolicyEngine.evaluate_compliance(input_data)
                
                for rule in compliance_results:
                    if rule["status"] == "COMPLIANT":
                        st.success(f"✅ **{rule['policy']}**: {rule['domain']} (Actual: {rule['actual']})")
                    elif rule["status"] == "WARNING":
                        st.warning(f"⚠️ **{rule['policy']}**: {rule['domain']} (Actual: {rule['actual']}) - *{rule['requirement']}*")
                    else:
                        st.error(f"❌ **{rule['policy']}**: {rule['domain']} (Actual: {rule['actual']}) - *{rule['requirement']}*")
                # ----------------------------------------
                # ------------------------------------
                
                # Show probabilities
                st.subheader("Probability Breakdown")
                prob_df = pd.DataFrame({
                    'Risk Level': list(prediction['probabilities'].keys()),
                    'Probability': list(prediction['probabilities'].values())
                })
                st.dataframe(prob_df.style.format({'Probability': '{:.2%}'}))

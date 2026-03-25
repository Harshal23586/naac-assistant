import pandas as pd
import numpy as np
from datetime import datetime
from typing import Optional, Dict


def get_document_requirements_by_parameters(approval_type):
    """Get document requirements organized by parameters"""
    # This function is now in document_analysis.py, but we can keep it here too
    # for other modules to use if needed
    pass

def calculate_performance_percentile(score, inst_type, historical_data):
    """Calculate performance percentile within institution type"""
    type_data = historical_data[
        (historical_data['institution_type'] == inst_type) &
        (historical_data['year'] == 2023)
    ]
    
    if len(type_data) == 0:
        return 50.0
    
    return (type_data['performance_score'] < score).mean() * 100

def generate_approval_recommendation(performance_score: float, risk_level: str = "Medium Risk", doc_verification: bool = True, metrics_dict: Optional[Dict] = None) -> str:
    """Generate approval recommendation combining performance, predictive risk, statutory policy, and documents"""
    if performance_score >= 8.0:
        rec = "Full Approval - 5 Years"
    elif performance_score >= 7.0:
        rec = "Provisional Approval - 3 Years"
    elif performance_score >= 6.0:
        rec = "Conditional Approval - 1 Year"
    elif performance_score >= 5.0:
        rec = "Approval with Strict Monitoring - 1 Year"
    else:
        rec = "Rejection - Significant Improvements Required"
        
    # Statutory Override (Non-negotiable clauses)
    if metrics_dict:
        try:
            from core.policy_engine import StatutoryPolicyEngine
            compliance_results = StatutoryPolicyEngine.evaluate_compliance(metrics_dict)
            for rule in compliance_results:
                if rule['status'] == "NON_COMPLIANT" and rule['impact'] == "Core Approval Target":
                    rec = "Rejection - Statutory Policy Violation"
                    break
        except ImportError:
            pass
        
    # Downgrade based on predictive risk
    if risk_level in ["High Risk", "Critical Risk"]:
        if "Full" in rec or "Provisional" in rec:
            rec = "Conditional Approval - 1 Year"
            
    # Downgrade based on document verification
    if not doc_verification and "Rejection" not in rec:
        rec = "Approval with Strict Monitoring - 1 Year"
        
    return rec

def generate_decision_support_report(performance_score: float, risk_level: str, metrics_dict: Optional[Dict] = None) -> dict:
    """Generate detailed policy-aware AI decision support"""
    rec = generate_approval_recommendation(performance_score, risk_level, metrics_dict=metrics_dict)
    reasons = []
    policy_alignments = ["NEP 2020: Risk-adjusted assessment", "AICTE: Automatic downgrade upon risk detection"]
    
    if performance_score >= 8.0:
        reasons.append("High performance score qualifies for Full Approval.")
    elif performance_score >= 6.0:
        reasons.append("Moderate performance score requires provisional or conditional measures.")
    else:
        reasons.append("Low performance score dictates strict monitoring or rejection.")
        
    if risk_level in ["High Risk", "Critical Risk"]:
        reasons.append(f"Downgraded maximum approval due to Live Machine Learning Prediction: {risk_level} detected by Decision Tree Classifier.")
        
    # Extract precise reasons from explicit statutory checking
    if metrics_dict:
        try:
            from core.policy_engine import StatutoryPolicyEngine
            compliance_results = StatutoryPolicyEngine.evaluate_compliance(metrics_dict)
            for rule in compliance_results:
                if rule['status'] == "NON_COMPLIANT":
                    reasons.append(f"FAIL: {rule['policy']} -> {rule['domain']} actual value ({rule['actual']}) breaches mandatory requirement ({rule['requirement']})")
                    policy_alignments.append(f"Strict Enforcement: {rule['policy']}")
                elif rule['status'] == "WARNING":
                    reasons.append(f"MONITOR: {rule['policy']} -> {rule['domain']} limit is approaching dangerous thresholds ({rule['actual']}).")
                else:
                    policy_alignments.append(f"Compliant Checklist: {rule['policy']} verified.")
        except ImportError:
            pass
        
    return {
        "final_recommendation": rec,
        "policy_alignments": list(set(policy_alignments)),
        "reasons": reasons
    }

def assess_risk_level(performance_score):
    """Assess institutional risk level"""
    if performance_score >= 8.0:
        return "Low Risk"
    elif performance_score >= 6.5:
        return "Medium Risk"
    elif performance_score >= 5.0:
        return "High Risk"
    else:
        return "Critical Risk"

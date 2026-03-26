from typing import Dict, List, Any

class StatutoryPolicyEngine:
    """
    Evaluates institutional metrics against explicit Indian Higher Education statutory 
    guidelines including AICTE Handbook, UGC Quality Mandate, and NEP 2020 frameworks.
    """
    
    @staticmethod
    def evaluate_compliance(metrics: Dict[str, Any]) -> List[Dict[str, Any]]:
        results = []
        
        # Safely default variables if metrics dict is incomplete
        sfr = metrics.get('student_faculty_ratio', 20.0)
        phd_ratio = metrics.get('phd_faculty_ratio', 0.5)
        community = metrics.get('community_projects', 0)
        financial = metrics.get('financial_stability_score', 7.0)
        
        # 1. AICTE Student-Faculty Ratio Check
        if sfr <= 20.0:
            sfr_status = "COMPLIANT"
        elif sfr <= 25.0:
            sfr_status = "WARNING"
        else:
            sfr_status = "NON_COMPLIANT"
            
        results.append({
            "policy": "AICTE Clause 4.2.1",
            "domain": "Student-Faculty Ratio",
            "requirement": "Strict adherence to <= 20.0 ratio.",
            "actual": f"{sfr:.1f}",
            "status": sfr_status,
            "impact": "Core Approval Target"
        })
        
        # 2. UGC PhD Mandate Check
        if phd_ratio >= 0.40:
            phd_status = "COMPLIANT"
        elif phd_ratio >= 0.20:
            phd_status = "WARNING"
        else:
            phd_status = "NON_COMPLIANT"
            
        results.append({
            "policy": "UGC Quality Mandate",
            "domain": "Faculty Qualifications",
            "requirement": "Minimum 40% (0.40) of faculty must hold PhDs.",
            "actual": f"{phd_ratio:.2f}",
            "status": phd_status,
            "impact": "Core Approval Target"
        })
        
        # 3. NEP 2020 Holistic Education Check
        if community >= 2:
            community_status = "COMPLIANT"
        else:
            community_status = "WARNING"
            
        results.append({
            "policy": "NEP 2020 Directive",
            "domain": "Holistic & Multidisciplinary Education",
            "requirement": "Requires evidence of ongoing Community Engagement/Projects (> 2)",
            "actual": f"{community}",
            "status": community_status,
            "impact": "Auxiliary Target"
        })
        
        # 4. AICTE Financial Viability Standard
        if financial >= 6.0:
            fin_status = "COMPLIANT"
        elif financial >= 5.0:
            fin_status = "WARNING"
        else:
            fin_status = "NON_COMPLIANT"
            
        results.append({
            "policy": "AICTE Financial Viability",
            "domain": "Financial Stability",
            "requirement": "Financial Stability score must be >= 6.0/10.",
            "actual": f"{financial:.1f}",
            "status": fin_status,
            "impact": "Core Approval Target"
        })
        
        return results


from fastapi import APIRouter, Depends
from schemas import InstitutionMetrics
from services.policy_engine import StatutoryPolicyEngine
from services.auth import get_current_user

router = APIRouter()

@router.post("/evaluate")
def evaluate_policy_compliance(metrics: InstitutionMetrics, current_user: str = Depends(get_current_user)):
    """
    Evaluates institutional parameters securely against Indian Statutory targets 
    (AICTE, UGC, NEP 2020) and returns compliance results.
    """
    raw_dict = metrics.model_dump()
    rules_validation = StatutoryPolicyEngine.evaluate_compliance(raw_dict)
    
    # Check for blocking breaches
    is_blocked = any(r['status'] == 'NON_COMPLIANT' and r['impact'] == 'Core Approval Target' for r in rules_validation)
    
    return {
        "status": "success",
        "data": {
            "is_approval_blocked_by_statute": is_blocked,
            "evaluations": rules_validation
        }
    }


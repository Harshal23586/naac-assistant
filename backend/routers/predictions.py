from fastapi import APIRouter, HTTPException, Depends
from schemas import InstitutionMetrics
from services.inference import DecisionTreeInferenceService
from services.auth import get_current_user
import os

router = APIRouter()

# Resolve path relatively assuming uvicorn is run from within the backend/ folder
model_path = os.path.join(os.path.dirname(__file__), "../../models/decision_tree_model.pkl")
try:
    inference_service = DecisionTreeInferenceService(model_path=model_path)
except Exception as e:
    inference_service = None
    print(f"Warning: ML model not loaded during startup. {e}")

@router.post("/risk")
def predict_institutional_risk(metrics: InstitutionMetrics, current_user: str = Depends(get_current_user)):
    """
    Simulates the ML Decision Tree Inference to forecast 'Risk' based on provided stats.
    """
    if not inference_service:
        raise HTTPException(status_code=503, detail="Machine Learning model is not trained or loaded. Run the main app to generate the .pkl first.")
        
    try:
        raw_dict = metrics.model_dump()
        prediction_result = inference_service.predict(raw_dict)
        return {"status": "success", "data": prediction_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from services.inference import inference_service
from services.policy_engine import policy_engine
from services.nlp import faiss_engine

app = FastAPI(title="SUGAM AI Vector Engine", description="Handles ML Scoring, Institutional RAG Graph Vectors, and Deep Neural Deployments.", version="3.0.0")

class InferenceRequest(BaseModel):
    features: dict

class PolicyRequest(BaseModel):
    faculty_count: int
    infrastructure_score: int
    grant_funds: float

class NLPRequest(BaseModel):
    document_text: str
    query: str
    institution_data: dict = {}

class ExtractionRequest(BaseModel):
    document_text: str

class FraudRequest(BaseModel):
    records: list

@app.post("/predict")
def predict_approval(payload: InferenceRequest):
    try:
        result = inference_service.predict_approval(payload.features)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/policy/evaluate")
def evaluate_statutory_rules(payload: PolicyRequest):
    # Mapping structural inputs cleanly seamlessly safely securely natively.
    eval_data = {
        "total_faculty": payload.faculty_count,
        "campus_area_sqm": payload.infrastructure_score * 100,
        "grant_funds": payload.grant_funds
    }
    result = policy_engine.evaluate_compliance(eval_data)
    return result

@app.post("/nlp/rag")
def run_vector_rag(payload: NLPRequest):
    """Executes True Deep Semantic Similarity extraction perfectly relying upon Native FAISS indices natively cleanly safely!"""
    try:
        logging.info(f"Ingesting {len(payload.document_text)} char OCR arrays directly into Vector Index...")
        # Step 1: Push unstructured OCR logic physically into local FAISS Memory allocations safely!
        total_chunks = faiss_engine.ingest_document(payload.document_text)
        
        # Step 2: Extract Deep Dense Matches accurately overriding weak keyword mappings inherently!
        top_matches = faiss_engine.query_policy(payload.query, top_k=3)
        
        # Step 3: Stream exact extracted RAG Contexts explicitly into Universal LLM Synthesizers
        from services.generator import llm_engine
        generative_decision = llm_engine.generate_decision(top_matches, payload.institution_data, payload.query)
        
        return {
            "status": "success", 
            "extracted_nodes": top_matches,
            "vector_chunks": total_chunks,
            "query_resolved": payload.query,
            "generative_decision": generative_decision
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/nlp/extract")
def execute_document_intelligence(payload: ExtractionRequest):
    """Parses Raw Text natively extracting strict entities dynamically isolating JSON correctly smoothly!"""
    try:
        from services.ner_extractor import intelligent_extractor
        extracted_data = intelligent_extractor.extract_document_intelligence(payload.document_text)
        
        return {
            "status": "success",
            "intelligence_report": extracted_data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/nlp/fraud")
def execute_anomaly_audit(payload: FraudRequest):
    """Executes Deep Machine Learning Vectors detecting Explicit Institutional Fraud mathematically seamlessly properly!"""
    try:
        from services.anomaly_detector import fraud_engine
        security_report = fraud_engine.execute_audit(payload.records)
        
        return {
            "status": "success",
            "security_report": security_report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


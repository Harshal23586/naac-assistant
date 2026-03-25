from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SUGAM Workflow Engine", description="Dedicated State Machine tracking explicit AI and Human Institutional lifecycle approvals.", version="1.0.0")

VALID_TRANSITIONS = {
    "SUBMITTED": ["AI_DOCUMENT_VERIFICATION"],
    "AI_DOCUMENT_VERIFICATION": ["REVIEWER_ASSIGNMENT", "REJECTED"],
    "REVIEWER_ASSIGNMENT": ["AI_SCORING_PHASE", "REJECTED"],
    "AI_SCORING_PHASE": ["FINAL_DECISION", "REJECTED"],
    "FINAL_DECISION": ["APPROVED", "REJECTED"],
    "APPROVED": [],
    "REJECTED": []
}

@app.post("/pipelines/initiate", response_model=schemas.ApprovalPipeline)
def initiate_pipeline(request: schemas.PipelineCreate, db: Session = Depends(get_db)):
    db_pipeline = models.ApprovalPipeline(institution_id=request.institution_id, current_status="SUBMITTED")
    db.add(db_pipeline)
    db.commit()
    db.refresh(db_pipeline)
    return db_pipeline

@app.put("/pipelines/{pipeline_id}/advance", response_model=schemas.ApprovalPipeline)
def advance_pipeline(pipeline_id: int, request: schemas.PipelineStatusUpdate, db: Session = Depends(get_db)):
    db_pipeline = db.query(models.ApprovalPipeline).filter(models.ApprovalPipeline.id == pipeline_id).first()
    if not db_pipeline:
        raise HTTPException(status_code=404, detail="Pipeline target not found")
        
    current = db_pipeline.current_status
    target = request.new_status
    
    if target not in VALID_TRANSITIONS.get(current, []):
        raise HTTPException(status_code=400, detail=f"Illegal state transition from {current} to {target}. Must follow strict progression rules.")
        
    db_pipeline.current_status = target
    db.commit()
    db.refresh(db_pipeline)
    return db_pipeline

@app.post("/assignments/{pipeline_id}", response_model=schemas.ReviewerAssignment)
def assign_reviewer(pipeline_id: int, request: schemas.AssignmentCreate, db: Session = Depends(get_db)):
    db_pipeline = db.query(models.ApprovalPipeline).filter(models.ApprovalPipeline.id == pipeline_id).first()
    if not db_pipeline:
        raise HTTPException(status_code=404, detail="Pipeline target not found")
        
    db_assignment = models.ReviewerAssignment(
        pipeline_id=pipeline_id,
        reviewer_email=request.reviewer_email,
        role=request.role
    )
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

@app.get("/pipelines/{pipeline_id}", response_model=schemas.ApprovalPipeline)
def get_pipeline_details(pipeline_id: int, db: Session = Depends(get_db)):
    db_pipeline = db.query(models.ApprovalPipeline).filter(models.ApprovalPipeline.id == pipeline_id).first()
    if not db_pipeline:
        raise HTTPException(status_code=404, detail="Pipeline target not found")
    return db_pipeline

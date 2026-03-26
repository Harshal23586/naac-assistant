from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PipelineCreate(BaseModel):
    institution_id: int

class PipelineStatusUpdate(BaseModel):
    new_status: str

class AssignmentCreate(BaseModel):
    reviewer_email: str
    role: str

class ReviewerAssignment(AssignmentCreate):
    id: int
    pipeline_id: int
    class Config:
        from_attributes = True

class ApprovalPipeline(PipelineCreate):
    id: int
    current_status: str
    started_at: datetime
    updated_at: datetime
    assignments: List[ReviewerAssignment] = []
    class Config:
        from_attributes = True


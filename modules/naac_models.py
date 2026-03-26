from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict

class NAACApplication(BaseModel):
    id: str
    institution_id: str
    institution_name: str
    cycle: int = 1
    status: str = "draft"
    created_at: datetime = datetime.now()

class MetricResponse(BaseModel):
    id: str
    application_id: str
    metric_code: str
    metric_name: str
    criterion: int
    response: dict
    documents: List[str] = []

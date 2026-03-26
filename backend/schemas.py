from pydantic import BaseModel, Field
from typing import Optional

class InstitutionMetrics(BaseModel):
    # Core performance metrics required by the ML Decision Tree
    student_faculty_ratio: float = Field(..., description="E.g. 15.0 or 25.0", example=15.0)
    phd_faculty_ratio: float = Field(..., example=0.5)
    research_publications: int = Field(..., example=20)
    research_grants_amount: float = Field(..., example=10000000)
    industry_collaborations: int = Field(..., example=5)
    placement_rate: float = Field(..., example=75.0)
    compliance_score: float = Field(..., example=7.0)
    performance_score: float = Field(..., example=6.5)
    patents_filed: int = Field(default=2)
    digital_infrastructure_score: float = Field(default=6.0)
    library_volumes: int = Field(default=15000)
    laboratory_equipment_score: float = Field(default=7.0)
    financial_stability_score: float = Field(default=7.0)
    administrative_efficiency: float = Field(default=6.5)
    higher_education_rate: float = Field(default=20.0)
    entrepreneurship_cell_score: float = Field(default=6.0)
    community_projects: int = Field(default=5)
    rural_outreach_score: float = Field(default=6.0)
    inclusive_education_index: float = Field(default=6.5)


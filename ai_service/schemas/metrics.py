from pydantic import BaseModel

class InstitutionMetrics(BaseModel):
    student_faculty_ratio: float = 20.0
    phd_faculty_ratio: float = 0.5
    research_publications: int = 0
    research_grants_amount: float = 0.0
    industry_collaborations: int = 0
    placement_rate: float = 0.0
    compliance_score: float = 0.0
    performance_score: float = 0.0
    financial_stability_score: float = 7.0
    community_projects: int = 2


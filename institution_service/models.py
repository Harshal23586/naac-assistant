from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class InstitutionProfile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    establishment_year = Column(Integer)
    university_type = Column(String)

    faculty = relationship("FacultyRecord", back_populates="institution")
    history = relationship("HistoricalEvaluation", back_populates="institution")

class FacultyRecord(Base):
    __tablename__ = "faculty_data"

    id = Column(Integer, primary_key=True, index=True)
    institution_id = Column(Integer, ForeignKey("profiles.id"))
    department = Column(String, nullable=False)
    has_phd = Column(Boolean, default=False)
    professors_count = Column(Integer, default=1)

    institution = relationship("InstitutionProfile", back_populates="faculty")

class HistoricalEvaluation(Base):
    __tablename__ = "historical_records"

    id = Column(Integer, primary_key=True, index=True)
    institution_id = Column(Integer, ForeignKey("profiles.id"))
    year = Column(Integer)
    status = Column(String)
    ai_risk_score = Column(Float)

    institution = relationship("InstitutionProfile", back_populates="history")


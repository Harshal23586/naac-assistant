from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime
from database import Base

class ApprovalPipeline(Base):
    __tablename__ = "pipelines"

    id = Column(Integer, primary_key=True, index=True)
    institution_id = Column(Integer, index=True, nullable=False)
    current_status = Column(String, default="SUBMITTED", nullable=False)
    started_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    assignments = relationship("ReviewerAssignment", back_populates="pipeline")

class ReviewerAssignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    pipeline_id = Column(Integer, ForeignKey("pipelines.id"))
    reviewer_email = Column(String, nullable=False)
    role = Column(String, nullable=False)

    pipeline = relationship("ApprovalPipeline", back_populates="assignments")


from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
import datetime

class DocumentRecord(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True, nullable=False)
    version = Column(Integer, default=1, nullable=False)
    content_type = Column(String, nullable=False)
    extracted_text = Column(Text, nullable=True)
    uploaded_at = Column(DateTime, default=datetime.datetime.utcnow)

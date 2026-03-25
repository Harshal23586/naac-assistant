from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SUGAM Institution Service", description="Transactional profile controller preventing AI microservice timeouts.", version="1.0.0")

@app.post("/profiles/", response_model=schemas.Profile)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    db_profile = models.InstitutionProfile(**profile.model_dump())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

@app.get("/profiles/", response_model=List[schemas.Profile])
def get_profiles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.InstitutionProfile).offset(skip).limit(limit).all()

@app.get("/profiles/{profile_id}", response_model=schemas.Profile)
def get_profile(profile_id: int, db: Session = Depends(get_db)):
    db_profile = db.query(models.InstitutionProfile).filter(models.InstitutionProfile.id == profile_id).first()
    if not db_profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile

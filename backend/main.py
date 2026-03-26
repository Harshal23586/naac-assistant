from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import predictions, policy, auth

app = FastAPI(
    title="SUGAM API Backend",
    description="Microservice backend for Institutional Intelligence & AI Approvals.",
    version="1.0.0"
)

app.include_router(auth.router, tags=["Authentication"])
app.include_router(predictions.router, prefix="/api/v1/predict", tags=["AI Predictions"])
app.include_router(policy.router, prefix="/api/v1/policy", tags=["Statutory Compliance"])

import os

# Get allowed origins from environment variable
allowed_origins_str = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000")
allowed_origins = [origin.strip() for origin in allowed_origins_str.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "SUGAM API Gateway Backend"}


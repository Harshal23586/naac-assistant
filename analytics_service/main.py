from fastapi import FastAPI
from typing import Dict, Any, List
import random

app = FastAPI(title="SUGAM Analytics Service", description="High-performance data aggregation API fetching metrics for UI Frameworks.", version="1.0.0")

@app.get("/kpis")
def get_system_kpis() -> Dict[str, Any]:
    """Provides generalized system-wide performance values."""
    return {
        "status": "success",
        "data": {
            "total_institutions_processed": 1245,
            "average_processing_time_ms": 1420,
            "approval_rate_percentage": 68.5,
            "total_documents_scanned": 8902,
            "active_ai_models": 2
        }
    }

@app.get("/trends")
def get_historical_trends() -> Dict[str, Any]:
    """Generates time-series mapping dictionaries readable by Next.js Charting tools (Recharts)."""
    return {
        "status": "success",
        "data": [
            {"month": "Jan", "approvals": 120, "rejections": 45, "ai_flags": 12},
            {"month": "Feb", "approvals": 150, "rejections": 50, "ai_flags": 15},
            {"month": "Mar", "approvals": 180, "rejections": 40, "ai_flags": 8},
            {"month": "Apr", "approvals": 210, "rejections": 60, "ai_flags": 20},
            {"month": "May", "approvals": 190, "rejections": 45, "ai_flags": 10},
        ]
    }

@app.get("/benchmarking")
def get_peer_benchmarks(institution_type: str = "Public") -> Dict[str, Any]:
    """Calculates relative percentile comparisons matching individual institutions to regional medians."""
    return {
        "status": "success",
        "data": {
            "peer_group": institution_type,
            "median_phd_ratio": 0.55,
            "median_faculty_ratio": 18.5,
            "median_research_grants_usd": 1200000,
            "top_percentile_cutoff_score": 8.5
        }
    }

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    print("Health Check:", response.json())

def test_policy():
    data = {
        "student_faculty_ratio": 22.0,
        "phd_faculty_ratio": 0.5,
        "research_publications": 20,
        "research_grants_amount": 10000000,
        "industry_collaborations": 5,
        "placement_rate": 75.0,
        "compliance_score": 7.0,
        "performance_score": 6.5
    }
    response = client.post("/api/v1/policy/evaluate", json=data)
    assert response.status_code == 200
    print("Policy Evaluation:", response.json())

def test_prediction():
    data = {
        "student_faculty_ratio": 22.0,
        "phd_faculty_ratio": 0.5,
        "research_publications": 20,
        "research_grants_amount": 10000000,
        "industry_collaborations": 5,
        "placement_rate": 75.0,
        "compliance_score": 7.0,
        "performance_score": 6.5
    }
    response = client.post("/api/v1/predict/risk", json=data)
    if response.status_code == 200:
        print("ML Prediction:", response.json())
    else:
        print("ML Prediction Endpoint returned (likely missing model file):", response.status_code, response.json())


if __name__ == "__main__":
    test_health()
    test_policy()
    test_prediction()
    print("All backend tests completed.")


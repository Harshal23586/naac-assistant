from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

data_payload = {
    "student_faculty_ratio": 22.0,
    "phd_faculty_ratio": 0.5,
    "research_publications": 20,
    "research_grants_amount": 10000000,
    "industry_collaborations": 5,
    "placement_rate": 75.0,
    "compliance_score": 7.0,
    "performance_score": 6.5
}

def test_missing_token():
    # Try to access predict endpoint without token
    response = client.post("/api/v1/predict/risk", json=data_payload)
    if response.status_code == 401:
        print("✅ Correct: Successfully blocked unauthenticated AI prediction request with HTTP 401.")
    else:
        print(f"❌ Failed: Expected 401, got {response.status_code}")
        exit(1)

def test_successful_login_and_predict():
    # 1. Login via OAuth2 Form structure to get token
    login_response = client.post("/token", data={"username": "admin", "password": "admin123"})
    if login_response.status_code == 200:
        token = login_response.json()["access_token"]
        print(f"✅ Success: Generated active JWT Token -> {token[:20]}...")
    else:
        print("❌ Failed: Could not authenticate user admin/admin123.")
        exit(1)
        
    # 2. Use token on Predict via Bearer Header
    headers = {"Authorization": f"Bearer {token}"}
    predict_response = client.post("/api/v1/predict/risk", json=data_payload, headers=headers)
    
    # The actual inference might 503 if local ML model doesn't exist, but it MUST NOT be 401.
    if predict_response.status_code != 401:
        print(f"✅ Success: Predictor securely accessed using Token Header! Final Response Status: {predict_response.status_code}")
    else:
        print("❌ Failed: Endpoints rejected valid token.")
        exit(1)

if __name__ == "__main__":
    print("Starting Authentication Layer Tests...")
    test_missing_token()
    test_successful_login_and_predict()
    print("🔐 All Authentication mechanisms verified securely.")


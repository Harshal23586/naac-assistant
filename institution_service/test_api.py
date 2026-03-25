from fastapi.testclient import TestClient
from main import app
from database import Base, engine
import os

Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_institution_profiles():
    print("==========================================")
    print("  SUGAM Institution Service Diagnostics  ")
    print("==========================================")
    
    # 1. Create Profile
    payload = {
        "name": "Indian Institute of Technology, Bombay",
        "establishment_year": 1958,
        "university_type": "Public Technical Request"
    }
    
    print("Initiating POST /profiles/ payload injection...")
    resp = client.post("/profiles/", json=payload)
    
    if resp.status_code == 200:
        data = resp.json()
        print(f"✅ Success! Profile securely injected into SQLite Transaction Array.")
        print(f"   ► ID: {data['id']}")
        print(f"   ► Institution: {data['name']}")
    else:
        print(f"❌ Diagnostic POST Failure. Code: {resp.status_code}")
        print(resp.text)
        exit(1)

    # 2. Fetch Profile
    print("\nInitiating GET /profiles/ traversal...")
    fetch_resp = client.get("/profiles/")
    if fetch_resp.status_code == 200:
        records = fetch_resp.json()
        print(f"✅ Success! Fetched Database Registry! Internal Active Records: {len(records)}")
        print("==========================================")
    else:
        print("❌ Diagnostic GET Failure.")
        exit(1)

if __name__ == "__main__":
    test_institution_profiles()

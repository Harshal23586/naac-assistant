from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_analytics():
    print("==========================================")
    print("   SUGAM Analytics Service Diagnostics    ")
    print("==========================================")
    
    # KPIs
    kpis = client.get("/kpis")
    if kpis.status_code == 200:
        data = kpis.json()["data"]
        print(f"✅ Success! Fetched Systems KPIs: {data['total_institutions_processed']} Lifetime Institutions Processed.")
    else:
        print("❌ Diagnostic GET Failure on /kpis.")
        exit(1)

    # Trends
    trends = client.get("/trends")
    if trends.status_code == 200:
        data = trends.json()["data"]
        print(f"✅ Success! Time-Series Trends mapping fetched! (Tracked Blocks: {len(data)})")
    else:
        print("❌ Diagnostic GET Failure on /trends.")
        exit(1)
        
    print("==========================================")

if __name__ == "__main__":
    test_analytics()


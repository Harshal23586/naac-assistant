from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_workflow_state_machine():
    print("==========================================")
    print("   SUGAM Workflow Engine Diagnostics      ")
    print("==========================================")

    # 1. Initiate Pipeline
    payload = {"institution_id": 999}
    resp = client.post("/pipelines/initiate", json=payload)
    if resp.status_code == 200:
        pipeline = resp.json()
        pid = pipeline['id']
        print(f"✅ Built Application Pipeline ID: {pid} | Status: {pipeline['current_status']}")
    else:
        print(f"❌ Failed to Initiate Pipeline. {resp.text}")
        exit(1)

    # 2. Test valid transition (DRAFT -> AI_ANALYSIS)
    adv_payload_valid = {"new_status": "AI_ANALYSIS"}
    adv_resp1 = client.put(f"/pipelines/{pid}/advance", json=adv_payload_valid)
    if adv_resp1.status_code == 200:
        print(f"✅ Advanced Pipeline {pid} successfully to format: AI_ANALYSIS.")
    else:
        print(f"❌ Failed to shift Pipeline properly. {adv_resp1.text}")
        exit(1)

    # 3. Test invalid transition (AI_ANALYSIS -> APPROVED skip)
    adv_payload_invalid = {"new_status": "APPROVED"}
    adv_resp2 = client.put(f"/pipelines/{pid}/advance", json=adv_payload_invalid)
    if adv_resp2.status_code == 400:
        print(f"✅ State Machine explicitly BLOCKED illegal sequence jump (AI_ANALYSIS -> APPROVED).")
    else:
        print(f"❌ Diagnostic Failure! State Machine allowed an illegal skip! {adv_resp2.text}")
        exit(1)

    # 4. Assigner tracking
    assign_payload = {"reviewer_email": "auditor@aicte-sugam.gov.in", "role": "EXPERT_PANEL"}
    assign_resp = client.post(f"/assignments/{pid}", json=assign_payload)
    if assign_resp.status_code == 200:
        print(f"✅ Human Reviewer successfully mapped to Pipeline {pid}.")
    else:
        print(f"❌ Diagnostic Failure mapping User Assignment. {assign_resp.text}")
        exit(1)

    print("==========================================")

if __name__ == "__main__":
    test_workflow_state_machine()

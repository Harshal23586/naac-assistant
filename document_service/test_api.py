from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)

def test_upload():
    # Construct a minimal viable pure-text dummy PDF payload stream
    dummy_pdf_content = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> >> >> /Contents 4 0 R >>\nendobj\n4 0 obj\n<< /Length 55 >>\nstream\nBT\n/F1 24 Tf\n100 100 Td\n(Machine Learning Target Extract) Tj\nET\nendstream\nendobj\nxref\n0 5\n0000000000 65535 f\n0000000009 00000 n\n0000000058 00000 n\n0000000115 00000 n\n0000000282 00000 n\ntrailer\n<< /Size 5 /Root 1 0 R >>\nstartxref\n386\n%%EOF\n"
    
    pdf_path = "mock_extraction.pdf"
    with open(pdf_path, "wb") as f:
        f.write(dummy_pdf_content)

    print("Initiating Integration Request pointing at Local Document Microservice POST /upload ...")
    with open(pdf_path, "rb") as f:
        files = {"file": (pdf_path, f, "application/pdf")}
        response = client.post("/upload", files=files)
        
    os.remove(pdf_path)
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Success - Document IO Active! ID: {data['document_id']} | File: {data['filename']} | Version Matrix Tracking: v{data['version']}")
        print(f"✅ OCR Preview: {data['ocr_preview']}")
    else:
        print(f"❌ Diagnostic Failure. Payload Rejected. Code: {response.status_code}")
        exit(1)

if __name__ == "__main__":
    test_upload()


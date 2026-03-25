@echo off
echo =========================================================
echo SUGAM PLATFORM BOOTSTRAP (Local Native Testing Mode)
echo =========================================================

echo 1. Starting Core AI Backend (Port 8000)...
start cmd /k "cd backend && call ..\..\venv\Scripts\activate && uvicorn main:app --port 8000 --reload"

echo 2. Starting Document OCR Microservice (Port 8001)...
start cmd /k "cd document_service && call ..\..\venv\Scripts\activate && uvicorn main:app --port 8001 --reload"

echo 3. Starting AI Dedicated Microservice (Port 8002)...
start cmd /k "cd ai_service && call ..\..\venv\Scripts\activate && uvicorn main:app --port 8002 --reload"

echo 4. Starting Institution Service (Port 8003)...
start cmd /k "cd institution_service && call ..\..\venv\Scripts\activate && uvicorn main:app --port 8003 --reload"

echo 5. Starting Analytics Metric Dashboards (Port 8004)...
start cmd /k "cd analytics_service && call ..\..\venv\Scripts\activate && uvicorn main:app --port 8004 --reload"

echo 6. Starting Workflow Engine (Port 8005)...
start cmd /k "cd workflow_service && call ..\..\venv\Scripts\activate && uvicorn main:app --port 8005 --reload"

echo 7. Starting Streamlit Monolithic Platform (Port 8501)...
start cmd /k "cd streamlit_analytics && call ..\..\venv\Scripts\activate && streamlit run app.py --server.port 8501"

echo =========================================================
echo All microservices are launching in separate terminal windows!
echo - Core App API:     http://localhost:8000/docs
echo - Document API:     http://localhost:8001/docs
echo - Dedicated AI API: http://localhost:8002/docs
echo - Institution API:  http://localhost:8003/docs
echo - Analytics API:    http://localhost:8004/docs
echo - Workflow API:     http://localhost:8005/docs
echo - Streamlit Hub:    http://localhost:8501
echo =========================================================
pause

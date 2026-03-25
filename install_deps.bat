@echo off
echo Installing Backend Modules...
pip install -r backend/requirements.txt

echo Installing Document Service Modules...
pip install -r document_service/requirements.txt
pip install boto3 python-multipart

echo Installing AI Service Modules...
pip install -r ai_service/requirements.txt

echo Installing Institution Service Modules...
pip install -r institution_service/requirements.txt

echo Installing Workflow Service Modules...
pip install -r workflow_service/requirements.txt

echo Installing Analytics Service Modules...
pip install -r analytics_service/requirements.txt

echo Installing Frontend Next.js Modules...
cd frontend && npm install

echo ====================================
echo All dependencies installed securely!
echo ====================================
pause

FROM python:3.10-slim

WORKDIR /app

# Install dependencies before copying large source code to utilize Docker caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Run via Uvicorn targeting the FastAPI explicit endpoints
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

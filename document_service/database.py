import os
from pymongo import MongoClient
import logging

# Ensure Document persistence path exists physically
DOCUMENT_STORAGE_DIR = "./documents_storage"
os.makedirs(DOCUMENT_STORAGE_DIR, exist_ok=True)

# Parse Environment Variable OR fallback to MongoDB running safely locally via Port 27017
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")

client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
db = client['sugam_nosql']

# NoSQL Collections mapping
documents_collection = db['documents_metadata']
logs_collection = db['system_logs']

def get_db():
    try:
        # Check active node status safely prior to executing payload arrays
        client.admin.command('ping')
        return db
    except Exception as e:
        logging.error(f"Failed NoSQL Connection to MongoDB: {e}")
        return None

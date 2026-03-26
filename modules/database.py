# Enhanced Database Module for NAAC Accreditation Assistant
import sqlite3
import json
import os
import shutil
from datetime import datetime
import threading
import hashlib

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'naac_data.db')
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'uploads')

_local = threading.local()

class NAACDatabase:
    def __init__(self):
        self._ensure_dirs()
        self._connection = None
    
    def _ensure_dirs(self):
        """Ensure all required directories exist"""
        data_dir = os.path.dirname(DB_PATH)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        if not os.path.exists(UPLOAD_DIR):
            os.makedirs(UPLOAD_DIR)
    
    def _get_connection(self):
        """Get thread-specific database connection"""
        if not hasattr(_local, 'connection') or _local.connection is None:
            _local.connection = sqlite3.connect(DB_PATH, check_same_thread=False)
            _local.connection.row_factory = sqlite3.Row
            _local.cursor = _local.connection.cursor()
            self._create_tables(_local.connection, _local.cursor)
        return _local.connection, _local.cursor
    
    def _create_tables(self, conn, cursor):
        """Create all necessary tables"""
        
        # Institutions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS institutions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                institution_name TEXT,
                aishe_code TEXT UNIQUE,
                institution_type TEXT,
                orientation_category TEXT,
                legacy_category TEXT,
                address TEXT,
                city TEXT,
                state TEXT,
                pin TEXT,
                website TEXT,
                created_at TIMESTAMP,
                updated_at TIMESTAMP
            )
        ''')
        
        # NAAC Applications table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS naac_applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                institution_id INTEGER,
                cycle INTEGER DEFAULT 1,
                status TEXT DEFAULT 'draft',
                created_at TIMESTAMP,
                submitted_at TIMESTAMP,
                total_score REAL,
                binary_status TEXT,
                maturity_level INTEGER,
                completion_percentage REAL,
                FOREIGN KEY (institution_id) REFERENCES institutions (id)
            )
        ''')
        
        # Metric Responses table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS metric_responses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id INTEGER,
                metric_code TEXT,
                response TEXT,
                documents TEXT,
                auto_score REAL,
                user_score REAL,
                validated BOOLEAN DEFAULT 0,
                validation_notes TEXT,
                updated_at TIMESTAMP,
                FOREIGN KEY (application_id) REFERENCES naac_applications (id),
                UNIQUE(application_id, metric_code)
            )
        ''')
        
        # Documents metadata table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id INTEGER,
                metric_code TEXT,
                document_name TEXT,
                original_filename TEXT,
                file_path TEXT,
                file_size INTEGER,
                file_type TEXT,
                uploaded_at TIMESTAMP,
                FOREIGN KEY (application_id) REFERENCES naac_applications (id)
            )
        ''')
        
        # Backup/Restore table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS backups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                institution_id INTEGER,
                backup_file TEXT,
                backup_date TIMESTAMP,
                description TEXT
            )
        ''')
        
        conn.commit()
    
    def save_document(self, application_id, metric_code, file, original_filename):
        """Save uploaded document and return file info"""
        conn, cursor = self._get_connection()
        
        # Create upload directory for this application and metric
        metric_dir = os.path.join(UPLOAD_DIR, str(application_id), metric_code)
        os.makedirs(metric_dir, exist_ok=True)
        
        # Generate unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_filename = f"{timestamp}_{original_filename}"
        file_path = os.path.join(metric_dir, safe_filename)
        
        # Save file
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        
        # Get file size
        file_size = os.path.getsize(file_path)
        
        # Get file extension
        file_ext = os.path.splitext(original_filename)[1].lower()
        
        # Save to database
        cursor.execute('''
            INSERT INTO documents (
                application_id, metric_code, document_name, original_filename,
                file_path, file_size, file_type, uploaded_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            application_id, metric_code, safe_filename, original_filename,
            file_path, file_size, file_ext, datetime.now()
        ))
        
        doc_id = cursor.lastrowid
        conn.commit()
        
        return {
            'id': doc_id,
            'filename': safe_filename,
            'original': original_filename,
            'path': file_path,
            'size': file_size
        }
    
    def get_documents(self, application_id, metric_code):
        """Get all documents for a metric"""
        conn, cursor = self._get_connection()
        cursor.execute('''
            SELECT * FROM documents
            WHERE application_id = ? AND metric_code = ?
            ORDER BY uploaded_at DESC
        ''', (application_id, metric_code))
        
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    
    def delete_document(self, doc_id):
        """Delete a document from disk and database"""
        conn, cursor = self._get_connection()
        
        # Get file path first
        cursor.execute("SELECT file_path FROM documents WHERE id = ?", (doc_id,))
        row = cursor.fetchone()
        
        if row:
            # Delete from disk
            file_path = row['file_path']
            if os.path.exists(file_path):
                os.remove(file_path)
            
            # Delete from database
            cursor.execute("DELETE FROM documents WHERE id = ?", (doc_id,))
            conn.commit()
            return True
        
        return False
    
    def export_institution_data(self, institution_id):
        """Export all data for an institution as JSON"""
        conn, cursor = self._get_connection()
        
        # Get institution details
        cursor.execute("SELECT * FROM institutions WHERE id = ?", (institution_id,))
        institution = dict(cursor.fetchone())
        
        # Get applications
        cursor.execute("SELECT * FROM naac_applications WHERE institution_id = ?", (institution_id,))
        applications = [dict(row) for row in cursor.fetchall()]
        
        # Get responses for each application
        for app in applications:
            cursor.execute("SELECT * FROM metric_responses WHERE application_id = ?", (app['id'],))
            responses = [dict(row) for row in cursor.fetchall()]
            
            # Parse JSON responses
            for resp in responses:
                if resp['response']:
                    try:
                        resp['response'] = json.loads(resp['response'])
                    except:
                        pass
                if resp['documents']:
                    try:
                        resp['documents'] = json.loads(resp['documents'])
                    except:
                        pass
            
            app['responses'] = responses
            
            # Get documents
            cursor.execute("SELECT * FROM documents WHERE application_id = ?", (app['id'],))
            app['documents'] = [dict(row) for row in cursor.fetchall()]
        
        export_data = {
            'institution': institution,
            'applications': applications,
            'export_date': datetime.now().isoformat(),
            'version': '1.0'
        }
        
        return export_data
    
    def import_institution_data(self, export_data):
        """Import previously exported data"""
        conn, cursor = self._get_connection()
        
        # Check if institution exists
        aishe_code = export_data['institution']['aishe_code']
        cursor.execute("SELECT id FROM institutions WHERE aishe_code = ?", (aishe_code,))
        existing = cursor.fetchone()
        
        if existing:
            return {'success': False, 'error': 'Institution already exists'}
        
        # Insert institution
        institution = export_data['institution']
        del institution['id']
        del institution['created_at']
        del institution['updated_at']
        
        columns = ', '.join(institution.keys())
        placeholders = ', '.join(['?'] * len(institution))
        
        cursor.execute(f'''
            INSERT INTO institutions ({columns}, created_at, updated_at)
            VALUES ({placeholders}, ?, ?)
        ''', list(institution.values()) + [datetime.now(), datetime.now()])
        
        institution_id = cursor.lastrowid
        
        # Insert applications and their data
        for app in export_data['applications']:
            # Insert application
            app_data = {k: v for k, v in app.items() if k not in ['id', 'responses', 'documents', 'created_at', 'submitted_at']}
            app_data['institution_id'] = institution_id
            
            columns = ', '.join(app_data.keys())
            placeholders = ', '.join(['?'] * len(app_data))
            
            cursor.execute(f'''
                INSERT INTO naac_applications ({columns}, created_at)
                VALUES ({placeholders}, ?)
            ''', list(app_data.values()) + [datetime.now()])
            
            application_id = cursor.lastrowid
            
            # Insert responses
            for resp in app.get('responses', []):
                resp_data = {k: v for k, v in resp.items() if k not in ['id']}
                resp_data['application_id'] = application_id
                
                # Convert response to JSON if dict
                if isinstance(resp_data.get('response'), dict):
                    resp_data['response'] = json.dumps(resp_data['response'])
                if isinstance(resp_data.get('documents'), (list, dict)):
                    resp_data['documents'] = json.dumps(resp_data['documents'])
                
                columns = ', '.join(resp_data.keys())
                placeholders = ', '.join(['?'] * len(resp_data))
                
                cursor.execute(f'INSERT INTO metric_responses ({columns}) VALUES ({placeholders})', list(resp_data.values()))
        
        conn.commit()
        return {'success': True, 'institution_id': institution_id}
    
    def get_institution_stats(self, institution_id):
        """Get statistics for an institution"""
        conn, cursor = self._get_connection()
        
        # Get all applications
        cursor.execute('''
            SELECT a.*, 
                   (SELECT COUNT(*) FROM metric_responses WHERE application_id = a.id) as total_responses,
                   (SELECT COUNT(*) FROM metric_responses WHERE application_id = a.id AND response != '' AND response IS NOT NULL) as completed_responses
            FROM naac_applications a
            WHERE a.institution_id = ?
            ORDER BY a.created_at DESC
        ''', (institution_id,))
        
        applications = [dict(row) for row in cursor.fetchall()]
        
        # Get total metrics count
        from config.naac_config import METRICS
        total_metrics = len(METRICS)
        
        for app in applications:
            app['completion_rate'] = (app['completed_responses'] / total_metrics * 100) if total_metrics > 0 else 0
        
        return {
            'total_applications': len(applications),
            'applications': applications,
            'latest_completion': applications[0]['completion_rate'] if applications else 0,
            'latest_status': applications[0]['status'] if applications else None
        }

# Helper function
_db_instance = None

def get_db():
    global _db_instance
    if _db_instance is None:
        _db_instance = NAACDatabase()
    return _db_instance

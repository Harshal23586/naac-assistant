# Database Module for NAAC Accreditation Assistant
import sqlite3
import json
from datetime import datetime
import os
import threading

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'naac_data.db')

# Thread-local storage
_local = threading.local()

class NAACDatabase:
    def __init__(self):
        self._ensure_db_dir()
    
    def _get_connection(self):
        if not hasattr(_local, 'connection') or _local.connection is None:
            _local.connection = sqlite3.connect(DB_PATH, check_same_thread=False)
            _local.connection.row_factory = sqlite3.Row
            _local.cursor = _local.connection.cursor()
            self._create_tables(_local.connection, _local.cursor)
        return _local.connection, _local.cursor
    
    def _ensure_db_dir(self):
        data_dir = os.path.dirname(DB_PATH)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def _create_tables(self, conn, cursor):
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
        
        conn.commit()
    
    def save_institution(self, profile_data):
        """Save or update institution profile"""
        conn, cursor = self._get_connection()
        
        cursor.execute("SELECT id FROM institutions WHERE aishe_code = ?", (profile_data.get('aishe_code'),))
        existing = cursor.fetchone()
        
        now = datetime.now()
        
        if existing:
            cursor.execute('''
                UPDATE institutions SET
                    institution_name = ?, institution_type = ?,
                    orientation_category = ?, legacy_category = ?,
                    address = ?, city = ?, state = ?, pin = ?, website = ?,
                    updated_at = ?
                WHERE aishe_code = ?
            ''', (
                profile_data.get('name'), profile_data.get('type'),
                profile_data.get('orientation_category'), profile_data.get('legacy_category'),
                profile_data.get('address', ''), profile_data.get('city', ''),
                profile_data.get('state', ''), profile_data.get('pin', ''),
                profile_data.get('website', ''), now,
                profile_data.get('aishe_code')
            ))
            institution_id = existing[0]
        else:
            cursor.execute('''
                INSERT INTO institutions (
                    institution_name, aishe_code, institution_type,
                    orientation_category, legacy_category, address, city,
                    state, pin, website, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                profile_data.get('name'), profile_data.get('aishe_code'),
                profile_data.get('type'), profile_data.get('orientation_category'),
                profile_data.get('legacy_category'), profile_data.get('address', ''),
                profile_data.get('city', ''), profile_data.get('state', ''),
                profile_data.get('pin', ''), profile_data.get('website', ''),
                now, now
            ))
            institution_id = cursor.lastrowid
        
        conn.commit()
        return institution_id
    
    def get_institution(self, aishe_code):
        """Get institution by AISHE code"""
        conn, cursor = self._get_connection()
        cursor.execute("SELECT * FROM institutions WHERE aishe_code = ?", (aishe_code,))
        row = cursor.fetchone()
        if row:
            return dict(row)
        return None
    
    def get_institution_by_id(self, institution_id):
        """Get institution by ID"""
        conn, cursor = self._get_connection()
        cursor.execute("SELECT * FROM institutions WHERE id = ?", (institution_id,))
        row = cursor.fetchone()
        if row:
            return dict(row)
        return None
    
    def create_application(self, institution_id, cycle=1):
        """Create a new NAAC application"""
        conn, cursor = self._get_connection()
        now = datetime.now()
        cursor.execute('''
            INSERT INTO naac_applications (institution_id, cycle, status, created_at)
            VALUES (?, ?, ?, ?)
        ''', (institution_id, cycle, 'draft', now))
        
        application_id = cursor.lastrowid
        conn.commit()
        return application_id
    
    def get_active_application(self, institution_id):
        """Get the most recent active application for an institution"""
        conn, cursor = self._get_connection()
        cursor.execute('''
            SELECT * FROM naac_applications
            WHERE institution_id = ?
            ORDER BY created_at DESC LIMIT 1
        ''', (institution_id,))
        row = cursor.fetchone()
        
        if row:
            return dict(row)
        return None
    
    def save_metric_response(self, application_id, metric_code, response_data):
        """Save or update a metric response"""
        conn, cursor = self._get_connection()
        now = datetime.now()
        
        # Convert response to JSON string if it's a dict
        if isinstance(response_data.get('response'), dict):
            response_json = json.dumps(response_data.get('response'))
        else:
            response_json = response_data.get('response', '')
        
        documents_json = json.dumps(response_data.get('documents', []))
        
        cursor.execute('''
            INSERT OR REPLACE INTO metric_responses (
                application_id, metric_code, response, documents,
                auto_score, validated, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            application_id, metric_code, response_json,
            documents_json, response_data.get('auto_score'),
            response_data.get('validated', False), now
        ))
        
        conn.commit()
    
    def get_metric_responses(self, application_id):
        """Get all metric responses for an application"""
        conn, cursor = self._get_connection()
        cursor.execute("SELECT * FROM metric_responses WHERE application_id = ?", (application_id,))
        rows = cursor.fetchall()
        
        responses = {}
        
        for row in rows:
            data = dict(row)
            metric_code = data['metric_code']
            
            try:
                response_data = json.loads(data['response']) if data['response'] else {}
            except:
                response_data = data['response']
            
            try:
                documents = json.loads(data['documents']) if data['documents'] else []
            except:
                documents = []
            
            responses[metric_code] = {
                'response': response_data,
                'documents': documents,
                'auto_score': data['auto_score'],
                'validated': data['validated']
            }
        
        return responses
    
    def update_application_status(self, application_id, status, total_score=None, binary_status=None, maturity_level=None, completion_percentage=None):
        """Update application status"""
        conn, cursor = self._get_connection()
        cursor.execute('''
            UPDATE naac_applications SET
                status = ?, total_score = ?, binary_status = ?,
                maturity_level = ?, completion_percentage = ?, submitted_at = ?
            WHERE id = ?
        ''', (
            status, total_score, binary_status,
            maturity_level, completion_percentage,
            datetime.now() if status == 'submitted' else None,
            application_id
        ))
        conn.commit()
    
    def get_all_institutions(self):
        """Get list of all institutions"""
        conn, cursor = self._get_connection()
        cursor.execute("SELECT id, institution_name, aishe_code, updated_at FROM institutions ORDER BY updated_at DESC")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    
    def delete_institution(self, aishe_code):
        """Delete an institution and all related data"""
        conn, cursor = self._get_connection()
        
        # Get institution id
        institution = self.get_institution(aishe_code)
        if not institution:
            return False
        
        institution_id = institution['id']
        
        # Delete applications and their responses
        cursor.execute("SELECT id FROM naac_applications WHERE institution_id = ?", (institution_id,))
        applications = cursor.fetchall()
        
        for app in applications:
            cursor.execute("DELETE FROM metric_responses WHERE application_id = ?", (app['id'],))
        
        cursor.execute("DELETE FROM naac_applications WHERE institution_id = ?", (institution_id,))
        cursor.execute("DELETE FROM institutions WHERE id = ?", (institution_id,))
        
        conn.commit()
        return True

# Helper function
_db_instance = None

def get_db():
    global _db_instance
    if _db_instance is None:
        _db_instance = NAACDatabase()
    return _db_instance

# GitHub Storage Module for NAAC Accreditation Assistant
import os
import json
import base64
from datetime import datetime
import streamlit as st

# GitHub API Configuration
GITHUB_REPO = "Harshal23586/naac-assistant"
GITHUB_BRANCH = "main"
DATA_PATH = "data"

class GitHubStorage:
    def __init__(self):
        """Initialize GitHub storage with token from secrets"""
        self.token = st.secrets.get("GITHUB_TOKEN", "")
        self.repo = GITHUB_REPO
        self.branch = GITHUB_BRANCH
        self.data_path = DATA_PATH
    
    def _get_headers(self):
        """Get headers for GitHub API requests"""
        return {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def _make_request(self, url, method="GET", data=None):
        """Make GitHub API request"""
        import requests
        
        headers = self._get_headers()
        
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=data)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            return None
        
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        elif response.status_code == 404:
            return None
        else:
            st.error(f"GitHub API Error: {response.status_code} - {response.text}")
            return None
    
    def _get_file_sha(self, file_path):
        """Get SHA of existing file (required for updates)"""
        url = f"https://api.github.com/repos/{self.repo}/contents/{file_path}"
        result = self._make_request(url)
        if result and 'sha' in result:
            return result['sha']
        return None
    
    def save_institution(self, institution_data):
        """Save institution profile to GitHub"""
        file_path = f"{self.data_path}/institutions/{institution_data['aishe_code']}.json"
        
        # Prepare data
        data = {
            'aishe_code': institution_data['aishe_code'],
            'institution_name': institution_data.get('name'),
            'institution_type': institution_data.get('type'),
            'orientation_category': institution_data.get('orientation_category'),
            'legacy_category': institution_data.get('legacy_category'),
            'address': institution_data.get('address', ''),
            'city': institution_data.get('city', ''),
            'state': institution_data.get('state', ''),
            'pin': institution_data.get('pin', ''),
            'website': institution_data.get('website', ''),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        
        content = json.dumps(data, indent=2)
        encoded_content = base64.b64encode(content.encode()).decode()
        
        # Check if file exists
        sha = self._get_file_sha(file_path)
        
        # Prepare payload
        payload = {
            "message": f"Update institution {institution_data['aishe_code']}",
            "content": encoded_content,
            "branch": self.branch
        }
        
        if sha:
            payload["sha"] = sha
        
        url = f"https://api.github.com/repos/{self.repo}/contents/{file_path}"
        result = self._make_request(url, "PUT", payload)
        
        return result is not None
    
    def get_institution(self, aishe_code):
        """Get institution profile from GitHub"""
        file_path = f"{self.data_path}/institutions/{aishe_code}.json"
        url = f"https://api.github.com/repos/{self.repo}/contents/{file_path}"
        
        result = self._make_request(url)
        if result and 'content' in result:
            content = base64.b64decode(result['content']).decode()
            return json.loads(content)
        return None
    
    def save_application(self, aishe_code, cycle, application_data):
        """Save NAAC application data"""
        file_path = f"{self.data_path}/applications/{aishe_code}_cycle_{cycle}.json"
        
        data = {
            'aishe_code': aishe_code,
            'cycle': cycle,
            'status': application_data.get('status', 'draft'),
            'responses': application_data.get('responses', {}),
            'total_score': application_data.get('total_score'),
            'binary_status': application_data.get('binary_status'),
            'maturity_level': application_data.get('maturity_level'),
            'completion_percentage': application_data.get('completion_percentage'),
            'updated_at': datetime.now().isoformat(),
            'created_at': application_data.get('created_at', datetime.now().isoformat())
        }
        
        content = json.dumps(data, indent=2)
        encoded_content = base64.b64encode(content.encode()).decode()
        
        sha = self._get_file_sha(file_path)
        
        payload = {
            "message": f"Update application {aishe_code} Cycle {cycle}",
            "content": encoded_content,
            "branch": self.branch
        }
        
        if sha:
            payload["sha"] = sha
        
        url = f"https://api.github.com/repos/{self.repo}/contents/{file_path}"
        result = self._make_request(url, "PUT", payload)
        
        return result is not None
    
    def get_application(self, aishe_code, cycle=1):
        """Get NAAC application data"""
        file_path = f"{self.data_path}/applications/{aishe_code}_cycle_{cycle}.json"
        url = f"https://api.github.com/repos/{self.repo}/contents/{file_path}"
        
        result = self._make_request(url)
        if result and 'content' in result:
            content = base64.b64decode(result['content']).decode()
            return json.loads(content)
        return None
    
    def save_metric_response(self, aishe_code, cycle, metric_code, response_data):
        """Save a single metric response"""
        # Get existing application data
        app_data = self.get_application(aishe_code, cycle) or {
            'responses': {},
            'status': 'draft',
            'created_at': datetime.now().isoformat()
        }
        
        # Update the response
        app_data['responses'][metric_code] = {
            'response': response_data.get('response'),
            'documents': response_data.get('documents', []),
            'updated_at': datetime.now().isoformat()
        }
        
        # Update completion percentage
        from config.naac_config import METRICS
        total_metrics = len(METRICS)
        completed = sum(1 for r in app_data['responses'].values() if r.get('response') and r.get('response') != '')
        app_data['completion_percentage'] = (completed / total_metrics * 100) if total_metrics > 0 else 0
        
        # Save back
        return self.save_application(aishe_code, cycle, app_data)
    
    def get_metric_responses(self, aishe_code, cycle=1):
        """Get all metric responses"""
        app_data = self.get_application(aishe_code, cycle)
        if app_data:
            return app_data.get('responses', {})
        return {}
    
    def upload_document(self, aishe_code, cycle, metric_code, file):
        """Upload a document to GitHub"""
        from config.naac_config import METRICS
        
        # Get existing application data
        app_data = self.get_application(aishe_code, cycle) or {'responses': {}}
        
        # Create documents directory structure
        file_path = f"{self.data_path}/uploads/{aishe_code}/cycle_{cycle}/{metric_code}/{file.name}"
        
        # Read file content
        content = file.read()
        encoded_content = base64.b64encode(content).decode()
        
        # Check if file exists
        sha = self._get_file_sha(file_path)
        
        payload = {
            "message": f"Upload document for {aishe_code} - {metric_code}",
            "content": encoded_content,
            "branch": self.branch
        }
        
        if sha:
            payload["sha"] = sha
        
        url = f"https://api.github.com/repos/{self.repo}/contents/{file_path}"
        result = self._make_request(url, "PUT", payload)
        
        if result:
            # Update metric response with document reference
            metric_response = app_data['responses'].get(metric_code, {})
            documents = metric_response.get('documents', [])
            if file.name not in documents:
                documents.append(file.name)
                metric_response['documents'] = documents
                app_data['responses'][metric_code] = metric_response
                
                # Save updated application data
                self.save_application(aishe_code, cycle, app_data)
            
            return True
        
        return False
    
    def get_documents(self, aishe_code, cycle, metric_code):
        """Get list of documents for a metric"""
        app_data = self.get_application(aishe_code, cycle)
        if app_data and metric_code in app_data.get('responses', {}):
            return app_data['responses'][metric_code].get('documents', [])
        return []
    
    def get_document_url(self, aishe_code, cycle, metric_code, filename):
        """Get raw URL for a document"""
        return f"https://raw.githubusercontent.com/{self.repo}/{self.branch}/{self.data_path}/uploads/{aishe_code}/cycle_{cycle}/{metric_code}/{filename}"
    
    def export_all_data(self, aishe_code):
        """Export all data for an institution"""
        # Get institution profile
        institution = self.get_institution(aishe_code)
        
        # Get all applications
        applications = []
        for cycle in range(1, 5):  # Cycles 1-4
            app = self.get_application(aishe_code, cycle)
            if app:
                applications.append(app)
        
        export_data = {
            'institution': institution,
            'applications': applications,
            'export_date': datetime.now().isoformat(),
            'version': '2.0'
        }
        
        return export_data
    
    def import_all_data(self, export_data):
        """Import previously exported data"""
        # Save institution
        institution = export_data['institution']
        self.save_institution(institution)
        
        # Save applications
        for app in export_data['applications']:
            self.save_application(
                institution['aishe_code'],
                app.get('cycle', 1),
                app
            )
        
        return True

# Helper function
_storage_instance = None

def get_storage():
    """Get GitHub storage instance"""
    global _storage_instance
    if _storage_instance is None:
        _storage_instance = GitHubStorage()
    return _storage_instance

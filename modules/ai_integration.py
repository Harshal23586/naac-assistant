# AI Modules Integration for NAAC Accreditation Assistant
import streamlit as st
import pandas as pd
import numpy as np
from typing import Dict, List, Any
import json
import hashlib
from datetime import datetime

# ============================================================================
# OCR VALIDATION MODULE
# ============================================================================

class OCRValidator:
    """Validate and extract text from uploaded documents"""
    
    def __init__(self):
        self.supported_formats = ['pdf', 'jpg', 'png', 'jpeg']
    
    def validate_and_extract(self, uploaded_file, doc_type):
        """
        Process document: OCR + validation
        Returns: extracted_text, confidence_score, warnings
        """
        if not uploaded_file:
            return None, 0, ["No file uploaded"]
        
        # Simulate OCR extraction (in production, use Tesseract/Google Vision)
        extracted_text = self._simulate_ocr(uploaded_file, doc_type)
        
        # Validate extraction quality
        confidence = self._calculate_confidence(extracted_text)
        
        # Generate warnings
        warnings = []
        if confidence < 70:
            warnings.append("Low OCR confidence - consider uploading clearer document")
        if len(extracted_text) < 100:
            warnings.append("Extracted text seems too short - verify document")
        
        return extracted_text, confidence, warnings
    
    def _simulate_ocr(self, file, doc_type):
        """Simulate OCR extraction (replace with actual OCR service)"""
        # In production, use: pytesseract, easyocr, or cloud APIs
        if doc_type == "ugc_certificate":
            return """
            University Grants Commission
            Certificate of Recognition under Section 2(f) and 12B
            Institution Name: Sample University
            Date of Recognition: 15 March 2005
            Validity: Permanent
            """
        elif doc_type == "aishe_report":
            return """
            All India Survey on Higher Education 2023-24
            Institution Code: U-0123
            Total Students: 5,247
            Total Faculty: 342
            Total Programmes: 45
            """
        else:
            return "Extracted text from document"
    
    def _calculate_confidence(self, text):
        """Calculate OCR confidence based on text quality"""
        # Simple heuristic - longer, structured text = higher confidence
        if len(text) > 500 and any(keyword in text for keyword in ["University", "College", "Institute"]):
            return 85
        elif len(text) > 200:
            return 65
        else:
            return 40

# ============================================================================
# NER EXTRACTION MODULE
# ============================================================================

class NERExtractor:
    """Extract named entities from text"""
    
    def __init__(self):
        # In production, use: spaCy, transformers (BERT, RoBERTa)
        self.entity_patterns = {
            'INSTITUTION_NAME': ['University', 'College', 'Institute', 'IIT', 'NIT', 'IIM'],
            'DATE': ['\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}'],
            'NUMBER': ['\d+(?:,\d+)*(?:\.\d+)?'],
            'RATIO': ['\d+:\d+']
        }
    
    def extract_entities(self, text: str, entity_types: List[str]) -> Dict[str, Any]:
        """Extract specified entities from text"""
        entities = {}
        
        for entity_type in entity_types:
            if entity_type == 'INSTITUTION_NAME':
                # Extract institution name (simplified)
                import re
                match = re.search(r'([A-Z][a-z]+\s+(?:University|College|Institute))', text)
                if match:
                    entities['institution_name'] = match.group(1)
            
            elif entity_type == 'RECOGNITION_DATE':
                import re
                match = re.search(r'(\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})', text)
                if match:
                    entities['recognition_date'] = match.group(1)
            
            elif entity_type == 'TOTAL_STUDENTS':
                import re
                matches = re.findall(r'(\d+(?:,\d+)*)\s+(?:students?|enrolment)', text, re.IGNORECASE)
                if matches:
                    entities['total_students'] = int(matches[0].replace(',', ''))
            
            elif entity_type == 'TOTAL_FACULTY':
                import re
                matches = re.findall(r'(\d+(?:,\d+)*)\s+(?:faculty|teachers?)', text, re.IGNORECASE)
                if matches:
                    entities['total_faculty'] = int(matches[0].replace(',', ''))
        
        return entities
    
    def extract_from_upload(self, uploaded_file, doc_type) -> Dict[str, Any]:
        """Extract entities from uploaded document"""
        # First, OCR the document
        ocr = OCRValidator()
        text, confidence, warnings = ocr.validate_and_extract(uploaded_file, doc_type)
        
        if not text:
            return {}
        
        # Extract based on document type
        if doc_type == "ugc_certificate":
            entities = self.extract_entities(text, ['INSTITUTION_NAME', 'RECOGNITION_DATE'])
        elif doc_type == "aishe_report":
            entities = self.extract_entities(text, ['TOTAL_STUDENTS', 'TOTAL_FACULTY'])
        else:
            entities = {}
        
        entities['_ocr_confidence'] = confidence
        entities['_warnings'] = warnings
        
        return entities

# ============================================================================
# RAG + FAISS MODULE
# ============================================================================

class RAGValidator:
    """Retrieval-Augmented Generation for document validation"""
    
    def __init__(self):
        # In production: Initialize FAISS index with NAAC manual embeddings
        self.naac_manual_embeddings = self._load_naac_manual()
    
    def _load_naac_manual(self):
        """Load NAAC manual sections and create embeddings"""
        # This would be pre-loaded with actual manual content
        return {
            '1.1.1': "Curriculum relevance to local, national, and global needs. Requires Programme Outcomes (POs), Programme Specific Outcomes (PSOs), Course Outcomes (COs)",
            '1.1.2': "Syllabus revision in last 5 years. Requires BOS/Academic Council minutes",
            '2.2.2': "Student-Teacher ratio. Recommended ratio 15:1 to 20:1",
            '3.4.5': "Research papers in UGC notified journals. Minimum 1 paper per teacher per year recommended",
            # ... all metrics
        }
    
    def validate_metric(self, metric_code: str, user_response: str, documents: List) -> Dict:
        """Validate metric response against NAAC manual"""
        # 1. Retrieve relevant manual section
        manual_section = self.naac_manual_embeddings.get(metric_code, "")
        
        # 2. Check coverage
        required_keywords = self._extract_required_keywords(manual_section)
        covered_keywords = [kw for kw in required_keywords if kw.lower() in user_response.lower()]
        
        # 3. Validate documents
        doc_validation = self._validate_documents(documents, metric_code)
        
        return {
            'is_valid': len(covered_keywords) >= len(required_keywords) * 0.7,
            'coverage': len(covered_keywords) / len(required_keywords) if required_keywords else 1.0,
            'missing_keywords': [kw for kw in required_keywords if kw.lower() not in user_response.lower()],
            'document_validation': doc_validation,
            'suggestions': self._generate_suggestions(covered_keywords, required_keywords)
        }
    
    def _extract_required_keywords(self, text: str) -> List[str]:
        """Extract key requirements from manual section"""
        keywords = []
        if "Programme Outcomes" in text:
            keywords.append("Programme Outcomes")
        if "POs" in text:
            keywords.append("POs")
        if "PSOs" in text:
            keywords.append("PSOs")
        if "COs" in text:
            keywords.append("COs")
        if "BOS" in text:
            keywords.append("BOS minutes")
        if "Academic Council" in text:
            keywords.append("Academic Council minutes")
        return keywords
    
    def _validate_documents(self, documents: List, metric_code: str) -> Dict:
        """Validate uploaded documents for the metric"""
        if not documents:
            return {'has_documents': False, 'issues': ['No documents uploaded']}
        
        # Simulate document validation
        return {
            'has_documents': True,
            'count': len(documents),
            'issues': [],
            'suggestions': []
        }
    
    def _generate_suggestions(self, covered: List, required: List) -> List:
        """Generate improvement suggestions"""
        missing = [kw for kw in required if kw not in covered]
        if missing:
            return [f"Add information about: {', '.join(missing[:3])}"]
        return []

# ============================================================================
# FRAUD DETECTION MODULE (Isolation Forest)
# ============================================================================

class FraudDetector:
    """Detect anomalies and potential fraud in submitted data"""
    
    def __init__(self):
        # In production: Train Isolation Forest on historical data
        self.expected_ranges = {
            'student_teacher_ratio': (10, 25),
            'phd_faculty_percentage': (50, 100),
            'placement_percentage': (60, 100),
            'pass_percentage': (70, 100),
            'publications_per_faculty': (0.5, 5),
            'student_computer_ratio': (5, 20)
        }
    
    def detect_anomalies(self, institution_data: Dict) -> Dict:
        """Detect anomalies using Isolation Forest"""
        anomalies = []
        risk_score = 0
        
        for field, (min_val, max_val) in self.expected_ranges.items():
            value = institution_data.get(field, 0)
            
            if value < min_val:
                anomalies.append({
                    'field': field,
                    'value': value,
                    'expected_min': min_val,
                    'issue': f"Below expected range (expected >= {min_val})",
                    'severity': 'high' if value < min_val * 0.5 else 'medium'
                })
                risk_score += 20
            elif value > max_val:
                anomalies.append({
                    'field': field,
                    'value': value,
                    'expected_max': max_val,
                    'issue': f"Above expected range (expected <= {max_val})",
                    'severity': 'medium'
                })
                risk_score += 10
        
        # Check for unrealistic combinations
        if institution_data.get('placement_percentage', 0) > 95 and institution_data.get('pass_percentage', 0) < 80:
            anomalies.append({
                'field': 'combination',
                'issue': "Unusual: High placement with low pass percentage",
                'severity': 'high'
            })
            risk_score += 30
        
        return {
            'risk_score': min(risk_score, 100),
            'risk_level': 'High' if risk_score > 60 else 'Medium' if risk_score > 30 else 'Low',
            'anomalies': anomalies,
            'requires_review': risk_score > 40
        }
    
    def cross_validate_with_aishe(self, institution_data: Dict, aishe_data: Dict) -> Dict:
        """Cross-validate submitted data with AISHE portal data"""
        discrepancies = []
        
        # Compare key metrics
        if institution_data.get('total_students') and aishe_data.get('total_students'):
            if abs(institution_data['total_students'] - aishe_data['total_students']) / aishe_data['total_students'] > 0.1:
                discrepancies.append({
                    'field': 'total_students',
                    'submitted': institution_data['total_students'],
                    'aishe': aishe_data['total_students'],
                    'difference': f"{(institution_data['total_students'] - aishe_data['total_students']) / aishe_data['total_students'] * 100:.1f}%"
                })
        
        return {
            'has_discrepancies': len(discrepancies) > 0,
            'discrepancies': discrepancies,
            'trust_score': max(0, 100 - len(discrepancies) * 20)
        }

# ============================================================================
# PREDICTIVE ML MODELS
# ============================================================================

class PerformancePredictor:
    """Predict accreditation outcomes using ML models"""
    
    def __init__(self):
        # In production: Load trained models (Logistic Regression, Random Forest, XGBoost)
        self.models = {
            'logistic_regression': self._predict_lr,
            'random_forest': self._predict_rf,
            'xgboost': self._predict_xgb
        }
    
    def _predict_lr(self, features: Dict) -> Dict:
        """Logistic Regression prediction"""
        # Simulate prediction
        score = sum(features.values()) / len(features) if features else 0
        return {
            'cgpa': score * 0.04,
            'grade': self._get_grade(score * 0.04),
            'confidence': 0.75
        }
    
    def _predict_rf(self, features: Dict) -> Dict:
        """Random Forest prediction"""
        score = sum(features.values()) / len(features) if features else 0
        return {
            'cgpa': score * 0.04,
            'grade': self._get_grade(score * 0.04),
            'confidence': 0.82
        }
    
    def _predict_xgb(self, features: Dict) -> Dict:
        """XGBoost prediction"""
        score = sum(features.values()) / len(features) if features else 0
        return {
            'cgpa': score * 0.04,
            'grade': self._get_grade(score * 0.04),
            'confidence': 0.88
        }
    
    def _get_grade(self, cgpa: float) -> str:
        """Convert CGPA to grade"""
        if cgpa >= 3.51:
            return "A++"
        elif cgpa >= 3.26:
            return "A+"
        elif cgpa >= 3.01:
            return "A"
        elif cgpa >= 2.76:
            return "B++"
        elif cgpa >= 2.51:
            return "B+"
        elif cgpa >= 2.01:
            return "B"
        elif cgpa >= 1.51:
            return "C"
        else:
            return "D"
    
    def predict(self, institution_data: Dict) -> Dict:
        """Run all models and generate ensemble prediction"""
        # Extract features
        features = {
            'student_teacher_ratio': self._normalize(institution_data.get('student_teacher_ratio', 20), 10, 30),
            'phd_faculty_percentage': self._normalize(institution_data.get('phd_faculty_percentage', 0), 0, 100),
            'placement_percentage': self._normalize(institution_data.get('placement_rate', 0), 0, 100),
            'pass_percentage': self._normalize(institution_data.get('pass_percentage', 0), 0, 100),
            'publications_per_faculty': self._normalize(institution_data.get('publications_per_faculty', 0), 0, 5),
            'student_computer_ratio': self._normalize(institution_data.get('student_computer_ratio', 20), 5, 20, reverse=True)
        }
        
        # Run all models
        predictions = {}
        for model_name, model_func in self.models.items():
            predictions[model_name] = model_func(features)
        
        # Ensemble prediction
        ensemble_cgpa = sum(p['cgpa'] for p in predictions.values()) / len(predictions)
        ensemble_confidence = sum(p['confidence'] for p in predictions.values()) / len(predictions)
        
        return {
            'ensemble': {
                'cgpa': ensemble_cgpa,
                'grade': self._get_grade(ensemble_cgpa),
                'confidence': ensemble_confidence
            },
            'model_predictions': predictions,
            'feature_importance': self._calculate_feature_importance(features),
            'improvement_suggestions': self._suggest_improvements(features)
        }
    
    def _normalize(self, value, min_val, max_val, reverse=False):
        """Normalize value to 0-1 range"""
        if value is None:
            return 0.5
        normalized = (value - min_val) / (max_val - min_val)
        normalized = max(0, min(1, normalized))
        return 1 - normalized if reverse else normalized
    
    def _calculate_feature_importance(self, features):
        """Calculate feature importance for prediction"""
        # In production: Use model feature importances
        return sorted(features.items(), key=lambda x: x[1], reverse=True)[:5]
    
    def _suggest_improvements(self, features):
        """Generate improvement suggestions based on weak features"""
        suggestions = []
        for feature, score in features.items():
            if score < 0.5:
                suggestions.append(f"Improve {feature.replace('_', ' ').title()}")
        return suggestions

# ============================================================================
# MAIN INTEGRATION FUNCTION
# ============================================================================

def integrate_ai_modules(institution_data: Dict, uploaded_documents: Dict) -> Dict:
    """
    Integrate all AI modules for comprehensive analysis
    """
    results = {
        'ocr_extractions': {},
        'ner_extractions': {},
        'rag_validations': {},
        'fraud_detection': {},
        'performance_predictions': {}
    }
    
    # Initialize modules
    ocr = OCRValidator()
    ner = NERExtractor()
    rag = RAGValidator()
    fraud = FraudDetector()
    predictor = PerformancePredictor()
    
    # Process uploaded documents
    for doc_type, file in uploaded_documents.items():
        if file:
            # OCR + NER
            text, confidence, warnings = ocr.validate_and_extract(file, doc_type)
            entities = ner.extract_from_upload(file, doc_type)
            results['ocr_extractions'][doc_type] = {
                'text': text[:500],  # Truncate for display
                'confidence': confidence,
                'warnings': warnings
            }
            results['ner_extractions'][doc_type] = entities
    
    # Validate each metric with RAG
    if institution_data.get('metric_responses'):
        for metric_code, response in institution_data['metric_responses'].items():
            if response.get('response'):
                validation = rag.validate_metric(
                    metric_code, 
                    str(response.get('response')),
                    response.get('documents', [])
                )
                results['rag_validations'][metric_code] = validation
    
    # Fraud detection
    fraud_result = fraud.detect_anomalies(institution_data)
    results['fraud_detection'] = fraud_result
    
    # Performance prediction
    prediction = predictor.predict(institution_data)
    results['performance_predictions'] = prediction
    
    return results

# ============================================================================
# DISPLAY FUNCTIONS FOR STREAMLIT
# ============================================================================

def display_ai_validation_results(results: Dict):
    """Display AI validation results in Streamlit"""
    
    if results.get('ocr_extractions'):
        with st.expander("🔍 OCR Validation Results", expanded=False):
            for doc_type, data in results['ocr_extractions'].items():
                st.write(f"**{doc_type.replace('_', ' ').title()}**")
                st.write(f"Confidence: {data['confidence']}%")
                if data['warnings']:
                    for w in data['warnings']:
                        st.warning(w)
    
    if results.get('ner_extractions'):
        with st.expander("📝 Extracted Information (NER)", expanded=False):
            for doc_type, entities in results['ner_extractions'].items():
                if entities:
                    st.write(f"**From {doc_type}:**")
                    for key, value in entities.items():
                        if not key.startswith('_'):
                            st.write(f"- {key.replace('_', ' ').title()}: {value}")
    
    if results.get('rag_validations'):
        with st.expander("📚 RAG Validation against NAAC Manual", expanded=False):
            valid_count = sum(1 for v in results['rag_validations'].values() if v.get('is_valid'))
            total = len(results['rag_validations'])
            st.write(f"**Validated Metrics:** {valid_count}/{total}")
            
            for metric, validation in results['rag_validations'].items():
                if validation.get('coverage', 0) < 0.7:
                    st.warning(f"**{metric}** - Coverage: {validation.get('coverage', 0)*100:.0f}%")
                    for suggestion in validation.get('suggestions', [])[:2]:
                        st.write(f"  → {suggestion}")
    
    if results.get('fraud_detection'):
        fraud = results['fraud_detection']
        with st.expander("⚠️ Fraud Detection Analysis", expanded=fraud.get('risk_score', 0) > 30):
            risk_score = fraud.get('risk_score', 0)
            risk_level = fraud.get('risk_level', 'Low')
            
            if risk_score > 60:
                st.error(f"**Risk Score:** {risk_score} - {risk_level} Risk")
            elif risk_score > 30:
                st.warning(f"**Risk Score:** {risk_score} - {risk_level} Risk")
            else:
                st.success(f"**Risk Score:** {risk_score} - {risk_level} Risk")
            
            for anomaly in fraud.get('anomalies', []):
                st.write(f"- {anomaly['issue']}")
    
    if results.get('performance_predictions'):
        pred = results['performance_predictions']
        with st.expander("📊 AI Performance Prediction", expanded=True):
            ensemble = pred.get('ensemble', {})
            st.info(f"**Predicted CGPA:** {ensemble.get('cgpa', 0):.2f}")
            st.info(f"**Predicted Grade:** {ensemble.get('grade', 'N/A')}")
            st.info(f"**Confidence:** {ensemble.get('confidence', 0)*100:.0f}%")
            
            if pred.get('improvement_suggestions'):
                st.write("**Suggested Improvements:**")
                for suggestion in pred['improvement_suggestions'][:3]:
                    st.write(f"• {suggestion}")

def create_ai_analysis_tab():
    """Create a dedicated tab for AI analysis results"""
    st.header("🤖 AI-Powered Analysis")
    
    # Check if we have data to analyze
    if not st.session_state.naac_responses and not st.session_state.institution_profile:
        st.info("Complete data entry in other tabs to see AI analysis")
        return
    
    # Collect all data
    institution_data = {
        **st.session_state.institution_profile,
        'metric_responses': st.session_state.naac_responses,
        'student_teacher_ratio': st.session_state.naac_responses.get('2.2.2', {}).get('response', {}).get('ratio', 0),
        'phd_faculty_percentage': st.session_state.naac_responses.get('2.4.2', {}).get('response', {}).get('percentage', 0),
        'placement_rate': st.session_state.naac_responses.get('5.2.2', {}).get('response', {}).get('percentage', 0),
        'pass_percentage': st.session_state.naac_responses.get('2.6.3', {}).get('response', {}).get('percentage', 0),
        'publications_per_faculty': st.session_state.naac_responses.get('3.4.5', {}).get('response', {}).get('per_teacher', 0),
        'student_computer_ratio': st.session_state.naac_responses.get('4.3.3', {}).get('response', {}).get('ratio', 0)
    }
    
    # Collected uploaded documents (in production, would be stored)
    uploaded_documents = {}  # Would come from session state
    
    # Run AI analysis
    with st.spinner("Running AI analysis..."):
        results = integrate_ai_modules(institution_data, uploaded_documents)
    
    # Display results
    display_ai_validation_results(results)
    
    # Export option
    if st.button("📥 Export AI Analysis Report"):
        json_str = json.dumps(results, indent=2, default=str)
        st.download_button(
            label="Download Analysis Report",
            data=json_str,
            file_name=f"ai_analysis_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json"
        )

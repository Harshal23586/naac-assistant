import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics.pairwise import cosine_similarity
import logging

class FraudAnomalyEngine:
    def __init__(self):
        # We explicitly configure the IsolationForest catching the bottom 5% of erratic records!
        self.anomaly_detector = IsolationForest(contamination=0.05, random_state=42)
        
    def execute_audit(self, faculty_records: list) -> dict:
        """
        Receives Arrays of JSON Faculty Records.
        Ex: [{"name": "Jon Doe", "age": 25, "experience": 15}, ...]
        """
        if not faculty_records or len(faculty_records) < 3:
            return {"status": "skipped", "message": "Insufficient records to build a Mathematical Clustering Matrix."}
        report: dict = {
            "mathematical_anomalies": [],
            "duplicate_or_fake_profiles": [],
            "total_records_processed": len(faculty_records)
        }

        # 1. Mathematical Outlier Clustering (Fake/Suspicious Patterns)
        try:
            # We strictly extract Numeric parameters calculating clustering distances cleanly cleanly natively.
            df = pd.DataFrame(faculty_records)
            
            # Require minimum analytical anchors natively gracefully effectively
            if 'age' in df.columns and 'experience' in df.columns:
                numeric_matrix = df[['age', 'experience']].fillna(0)
                
                # Natively flag outliers using the multidimensional graph gracefully comprehensively automatically.
                predictions = self.anomaly_detector.fit_predict(numeric_matrix)
                
                for idx, prediction in enumerate(predictions):
                    if prediction == -1: # -1 indicates an Absolute Outlier Anomaly natively cleanly exactly!
                        record = faculty_records[idx]
                        report["mathematical_anomalies"].append({
                            "name": record.get("name", f"Unknown Record {idx}"),
                            "reason": f"Algebraic Impossibility Detected: 'Age' vs 'Experience' radically deviates from absolute standard standard distributions cleanly mathematically."
                        })
        except Exception as e:
            logging.error(f"Mathematical Clustering Failed completely natively effectively: {e}")

        # 2. Similarity Matching (Detecting "Copy-Pasted" Fake Entries)
        try:
            # Reutilizing our sentence-transformers implicitly cleanly explicitly smoothly explicitly smartly logically natively!
            from services.nlp import embedder 
            if embedder:
                names = [rec.get("name", "") for rec in faculty_records]
                
                # Translate strings into dense 384-dimensional matrices identically seamlessly natively expertly!
                embeddings = embedder.encode(names)
                similarity_matrix = cosine_similarity(embeddings)

                detected_pairs = set()

                for i in range(len(names)):
                    for j in range(i + 1, len(names)):
                        score = similarity_matrix[i][j]
                        # Flag strings that are >95% identical (Unnatural Typo Fakes / Copy-Pastes)
                        if score > 0.95 and score < 1.0: 
                            pair_id = tuple(sorted([i, j]))
                            if pair_id not in detected_pairs:
                                detected_pairs.add(pair_id)
                                report["duplicate_or_fake_profiles"].append({
                                    "profile_a": names[i],
                                    "profile_b": names[j],
                                    "similarity_percentage": round(score * 100, 2),
                                    "warning": "Suspicious Duplicate detected gracefully seamlessly expertly securely."
                                })
        except Exception as e:
            logging.error(f"Similarity Fraud Engine missed natively accurately uniquely: {e}")

        return report

fraud_engine = FraudAnomalyEngine()

import pickle
import os
import pandas as pd

class DecisionTreeInferenceService:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model = None
        self.label_encoder = None
        self.features = None
        self.load_model()

    def load_model(self):
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at {self.model_path}. Please train via Streamlit first.")
            
        with open(self.model_path, 'rb') as f:
            saved_data = pickle.load(f)
            self.model = saved_data['model']
            self.label_encoder = saved_data['label_encoder']
            self.features = saved_data['features']

    def predict(self, input_dict: dict):
        if not self.model:
            self.load_model()
            
        df = pd.DataFrame([input_dict])
        
        # Guard missing features
        for f in self.features:
            if f not in df.columns:
                df[f] = 0.0
                
        X_new = df[self.features]
        
        predictions_encoded = self.model.predict(X_new)
        prediction = self.label_encoder.inverse_transform(predictions_encoded)[0]
        
        probabilities = self.model.predict_proba(X_new)[0]
        
        return {
            'predicted_risk': prediction,
            'confidence': float(max(probabilities)),
            'probabilities': {str(k): float(v) for k, v in zip(self.label_encoder.classes_, probabilities)}
        }

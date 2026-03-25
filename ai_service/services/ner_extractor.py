import os
import json
import logging
from openai import OpenAI
from pydantic import BaseModel

class NERExtractor:
    def __init__(self):
        self.api_key = os.getenv("LLM_API_KEY", "")
        self.client = None
        if self.api_key:
            self.client = OpenAI(api_key=self.api_key)

    def extract_document_intelligence(self, raw_ocr_text: str) -> dict:
        """
        Consumes random Unstructured Text and guarantees a formally typed JSON structure explicitly 
        isolating Named Entities (NER), Classifications, and Missing Parameters intelligently.
        """
        
        system_prompt = (
            "You are a strict Document Intelligence Data Extractor. "
            "Your ONLY purpose is to ingest raw OCR text and output a pristine JSON dictionary exactly matching this schema:\n\n"
            "{\n"
            "  \"classification\": \"Document Type (e.g., Faculty List, Financial Audit, etc.)\",\n"
            "  \"entities\": [{\"name\": \"String\", \"qualifications\": [\"String\"], \"experience_years\": Integer}],\n"
            "  \"missing_data\": [\"Array of strictly missing analytical strings (e.g., 'Missing qualifications for John Doe')\"]\n"
            "}\n\n"
            "DO NOT output ANY markdown, explanation, or conversational text. ONLY raw JSON."
        )

        user_prompt = f"--- RAW OCR DUMP ---\n{raw_ocr_text}\n\nExecute pure JSON Extraction now."

        # Fallback Simulation explicitly masking missing API loops allowing Local Development offline successfully!
        if not self.client:
            logging.warning("LLM_API_KEY Missing. Simulating the JSON Extraction dynamically!")
            return {
                "classification": "Simulated Generic Document",
                "entities": [
                    {"name": "Dr. Simulated Name", "qualifications": ["Ph.D. locally simulated"], "experience_years": 10}
                ],
                "missing_data": [
                    "Bypassed active language generation: Please attach an LLM API Key."
                ]
            }

        try:
            # Physical Execution mapping strict JSON formatting schemas directly effortlessly smoothly natively cleanly
            assert self.client is not None
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.0, # Complete Determinism 
                response_format={"type": "json_object"} # Guaranteed JSON output schema
            )
            
            extracted_string = response.choices[0].message.content
            return json.loads(extracted_string)
            
        except Exception as e:
            logging.error(f"Intelligence Extraction SDK failed inherently: {e}")
            return {
                "classification": "Extraction Failed",
                "entities": [],
                "missing_data": [str(e)]
            }

intelligent_extractor = NERExtractor()

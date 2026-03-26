from typing import List, Dict, Any
import os
import logging
from openai import OpenAI

class LLMGenerator:
    def __init__(self):
        # We assume an agnostic wrapper API utilizing generic OpenAI constraints. 
        # (This securely maps any Gemini/Claude/ChatGPT key externally)
        self.api_key = os.getenv("LLM_API_KEY", "")
        self.client = None
        if self.api_key:
            self.client = OpenAI(api_key=self.api_key)

    def generate_decision(self, faiss_policies: List[str], institution_data: Dict[str, Any], regulatory_query: str) -> str:
        """
        Intersects High-Dimensional FAISS text chunks explicitly against raw JSON Institutional structures, prompting an LLM Engine intelligently!
        """
        compiled_policies = "\n".join(faiss_policies)
        
        system_prompt = (
            "You are an elite National Accreditation AICTE Auditor. "
            "You verify regulatory adherence systematically. "
            "Compare the retrieved Statutory Rule exactly against the provided Institutional Data JSON. "
            "Output precisely whether the institution passes or fails the regulation, and generate a concise 3-sentence explanation."
        )

        user_prompt = (
            f"Regulatory Query Subject: {regulatory_query}\n\n"
            f"--- Statutory Policy (from FAISS retrieval) ---\n"
            f"{compiled_policies}\n\n"
            f"--- Target Institution Metrics ---\n"
            f"{institution_data}\n\n"
            "Assess the institution."
        )

        # Fallback Simulation if API keys are not supplied explicitly (crucial for local offline development execution)
        if not self.client:
            logging.warning("LLM_API_KEY Missing. Simulating the Generative Decision Phase safely gracefully!")
            return f"**LLM Generation Bypassed** (API Key missing).\n\nBased exclusively on FAISS Retrieval, the policy states: '{faiss_policies[0][:100]}...'\n\nPlease inject a Cloud API Key to fully generate linguistic AI decisions."

        try:
            # Physical LLM Execution Loop inherently mapping the actual Augmented Generation structurally!
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo", # Interchangeable
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.2 # Keep it strictly deterministic/analytical 
            )
            return response.choices[0].message.content
        except Exception as e:
            logging.error(f"Generative API failed dynamically explicitly: {e}")
            return f"LLM Generation Error: {str(e)}"

llm_engine = LLMGenerator()


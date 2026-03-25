import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.analyzer import InstitutionalAIAnalyzer

analyzer = InstitutionalAIAnalyzer()

class DummyFile:
    def __init__(self, name, content):
        self.name = name
        self.content = content
        
    def getvalue(self):
        return self.content.encode('utf-8')

content = """
National Higher College
NAAC Grade: A+
NIRF Ranking: 45
Student Ratio: 15.5
Research Publications: 120
Library Volumes: 50000
"""

test_file = DummyFile("Curriculum_Framework_2023.txt", content)

res = analyzer.verify_document_authenticity([test_file])

print("VERIFICATION RESULT:", res)

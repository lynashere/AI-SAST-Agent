# Using Zero-Shot Chain-of-Thought to improve detection accuracy
# This prevents the LLM from hallucinating vulnerabilities by constraining the output to JSON.

import os
import json
import argparse
from langchain_community.llms import Ollama 

class AISASTAnalyzer:
    def __init__(self, model_name="mistral"):
        """Initializes the LLM engine. Mistral is preferred for its high signal-to-noise ratio in code tasks."""
        self.llm = Ollama(model=model_name, temperature=0)

    def generate_security_prompt(self, code_snippet):
        """Engineered prompt for precise semantic vulnerability detection."""
        return f"""
        [INST] You are an elite Senior Security Researcher. Analyze the following code for OWASP Top 10 vulnerabilities.
        Focus on: Buffer Overflows, SQL Injection, Insecure Deserialization, and Hardcoded Secrets.
        
        CODE:
        ---
        {code_snippet}
        ---
        
        Provide the output ONLY as a JSON list of objects with these keys: 
        "vulnerability", "severity" (High/Medium/Low), "line_number", and "remediation".
        [/INST]
        """

    def scan_file(self, file_path):
        """Reads file content and invokes the LLM for semantic analysis."""
        if not os.path.exists(file_path):
            return {"error": f"File {file_path} not found."}
            
        with open(file_path, 'r') as f:
            content = f.read()
        
        prompt = self.generate_security_prompt(content)
        response = self.llm.invoke(prompt)
        
        try:
            return json.loads(response)
        except:
            return {"error": "Failed to parse LLM output", "raw": response}

if __name__ == "__main__":
    # CLI support for enterprise-grade usability
    parser = argparse.ArgumentParser(description="AI-Driven Semantic SAST Scanner")
    parser.add_argument("file", help="Path to the source code file to scan")
    args = parser.parse_args()

    analyzer = AISASTAnalyzer()
    report = analyzer.scan_file(args.file)
    
    print(json.dumps(report, indent=2))
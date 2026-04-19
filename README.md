# AI-SAST-Agent: Semantic Vulnerability Scanner

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Model: Mistral-7B](https://img.shields.io/badge/Model-Mistral--7B-orange.svg)](https://mistral.ai/)

## Overview
**AI-SAST-Agent** is a next-generation Static Analysis Security Testing (SAST) tool that moves beyond traditional regex-based pattern matching. By leveraging Large Language Models (LLMs), it performs **semantic code analysis** to identify complex logical vulnerabilities, memory corruption, and insecure design patterns that standard tools often miss.

Built with a focus on high-performance environments (C++/Python), this tool is designed to integrate into modern DevSecOps pipelines, providing structured, actionable security intelligence.

---

## ✨ Key Features
* **Semantic Analysis:** Detects "intent-based" vulnerabilities (e.g., broken access control, logical bypasses).
* **OWASP Top 10 Mapping:** Automatically categorizes findings into OWASP categories and **CWE (Common Weakness Enumeration)** IDs.
* **Multi-Language Support:** Optimized for C++, Python, and JavaScript.
* **Automated Triage:** Generates structured **JSON reports** for seamless integration with banking and enterprise security dashboards.
* **Remediation Guidance:** Provides specific code fixes for every identified vulnerability.

---

## Technical Stack
* **Language:** Python 3.11
* **LLM Integration:** LangChain / Ollama (Mistral-7B-Instruct-v0.2)
* **Analysis Engine:** Zero-shot Chain-of-Thought (CoT) Prompting
* **Reporting:** JSON / Markdown

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have [Ollama](https://ollama.ai/) installed and the Mistral model pulled:
```bash
ollama pull mistral
```
### 2. Installation
```bash
git clone [https://github.com/yourusername/AI-SAST-Agent.git](https://github.com/yourusername/AI-SAST-Agent.git)
cd AI-SAST-Agent
pip install -r requirements.txt
```
### 3. Running a scan
```bash
python main.py --file ./samples/vulnerable_code.cpp --format json
```
## Example Output 
```JSON
[
  {
    "vulnerability": "Stack-based Buffer Overflow",
    "CWE": "CWE-121",
    "severity": "High",
    "line": 8,
    "remediation": "Use strncpy() or std::string to ensure bounds checking."
  },
  {
    "vulnerability": "Hardcoded Credentials",
    "CWE": "CWE-798",
    "severity": "High",
    "line": 14,
    "remediation": "Store sensitive keys in environment variables or a Secret Manager."
  }
]
```
## Why This Project?
Developed to improve the Signal-to-Noise ratio in security scanning. By utilizing AI to interpret code context, this tool empowers engineers to prioritize critical threats over false positives.

## License 
Distributed under the MIT License.

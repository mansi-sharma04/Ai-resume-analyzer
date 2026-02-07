# AI Resume Analyzer

A Generative AI–powered resume analysis tool that evaluates resume–job fit, identifies missing skills, and suggests improvements using a locally hosted LLM.

## Features
- Resume and job description comparison
- Match percentage estimation
- Identification of missing technical skills
- Resume improvement suggestions
- Recommended skills to learn

## Tech Stack
- Python
- Streamlit
- Generative AI
- Ollama (Local LLM)

## How It Works
1. Paste resume text
2. Paste job description
3. The local LLM analyzes alignment and generates insights

## Setup & Run Locally
```bash
pip install streamlit ollama
ollama pull llama3
streamlit run app.py

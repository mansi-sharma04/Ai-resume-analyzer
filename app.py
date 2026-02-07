import streamlit as st
import ollama

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")
st.write("Analyze your resume against a job description using a local LLM.")

resume_text = st.text_area("Paste your Resume here", height=200)
job_description = st.text_area("Paste Job Description here", height=200)

if st.button("Analyze Resume"):
    if resume_text.strip() == "" or job_description.strip() == "":
        st.warning("Please paste both Resume and Job Description.")
    else:
        with st.spinner("Analyzing..."):
            prompt = f"""
You are an AI resume evaluator.

Compare the resume with the job description and provide:
1. Match percentage (0–100)
2. Missing technical skills
3. Resume improvement suggestions
4. Suggested skills to learn

Resume:
{resume_text}

Job Description:
{job_description}

Respond in a clear, structured format.
"""

            response = ollama.chat(
                model="llama3",
                messages=[{"role": "user", "content": prompt}]
            )

            st.subheader("📊 Analysis Result")
            st.write(response["message"]["content"])

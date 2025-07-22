import streamlit as st
import os
from resume_parser import extract_text_from_pdf, extract_skills
from job_matcher import load_job_descriptions, match_jobs

SKILL_LIST = ["python", "machine learning", "deep learning", "tensorflow", "pytorch",
              "sql", "nlp", "flask", "django", "html", "css", "javascript", "react"]

st.set_page_config(page_title="Resume Matcher", layout="centered")
st.title("📄 AI Resume Parser & Job Match Recommender")

# File uploader
uploaded_file = st.file_uploader("Upload a Resume (PDF only)", type=["pdf"])

if uploaded_file:
    # 🛡 Ensure uploads/ folder exists
    os.makedirs("uploads", exist_ok=True)

    # 🧾 Save uploaded PDF locally
    resume_path = os.path.join("uploads", uploaded_file.name)
    with open(resume_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("Resume uploaded successfully.")

    # 🧠 Parse + Match
    text = extract_text_from_pdf(resume_path)
    found_skills = extract_skills(text, SKILL_LIST)
    st.write("### ✅ Extracted Skills:", ", ".join(found_skills))

    jobs = load_job_descriptions()
    match_result = match_jobs(found_skills, jobs)

    st.write("### 🧠 Job Match Scores:")
    st.dataframe(match_result)

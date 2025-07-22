import streamlit as st
import os
import pandas as pd
from resume_parser import extract_text_from_pdf, extract_skills
from job_matcher import load_job_descriptions, match_jobs

# Skill masterlist
SKILL_LIST = [
    "python", "machine learning", "deep learning", "tensorflow", "pytorch",
    "sql", "nlp", "flask", "django", "html", "css", "javascript", "react"
]

st.set_page_config(page_title="Resume Matcher", layout="centered")
st.title("📄 AI Resume Parser & Job Match Recommender")

uploaded_file = st.file_uploader("Upload a Resume (PDF only)", type=["pdf"])

if uploaded_file:
    resume_path = os.path.join("uploads", uploaded_file.name)
    with open(resume_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("Resume uploaded successfully.")
    text = extract_text_from_pdf(resume_path)
    found_skills = extract_skills(text, SKILL_LIST)
    st.write("### ✅ Extracted Skills:", ", ".join(found_skills))

    jobs = load_job_descriptions()
    match_result = match_jobs(found_skills, jobs)

    st.write("### 🧠 Job Match Scores:")
    df = pd.DataFrame(match_result, columns=["Job Role", "Match %"])
    st.dataframe(df)

    if df["Match %"].max() > 70:
        st.success("🎯 You're a great fit for some of these roles!")
    elif df["Match %"].max() > 40:
        st.info("👀 Somewhat aligned, maybe upskill a bit!")
    else:
        st.warning("😬 Resume could use stronger matching skills.")

import fitz  # PyMuPDF
import os
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()

def extract_skills(text, skill_list):
    found = [skill for skill in skill_list if skill.lower() in text]
    return list(set(found))

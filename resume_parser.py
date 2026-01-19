"""
resume_parser.py
----------------
This module handles resume parsing and skill extraction.
It reads PDF resumes and extracts relevant skills using NLP.
"""

import spacy
from PyPDF2 import PdfReader

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Central skill database (expandable)
SKILLS_DB = [
    "python", "java", "sql", "machine learning", "deep learning",
    "data analysis", "flask", "django", "html", "css",
    "javascript", "react", "node", "excel", "power bi", "api"
]

def extract_text_from_pdf(pdf_path):
    """
    Extracts raw text from a PDF resume.

    Args:
        pdf_path (str): Path to the PDF file

    Returns:
        str: Extracted resume text in lowercase
    """
    text = ""
    reader = PdfReader(pdf_path)

    # Loop through all pages and extract text
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    return text.lower()


def extract_skills(resume_text):
    """
    Extracts skills from resume text using keyword matching and NLP.

    Args:
        resume_text (str): Raw text from resume

    Returns:
        list: List of detected skills
    """
    doc = nlp(resume_text)
    skills_found = set()

    # Single-word skill detection
    for token in doc:
        token_text = token.text.lower()
        if token_text in SKILLS_DB:
            skills_found.add(token_text)

    # Multi-word skill detection (e.g., "machine learning")
    for skill in SKILLS_DB:
        if " " in skill and skill in resume_text:
            skills_found.add(skill)

    return list(skills_found)

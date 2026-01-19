"""
app.py
------
Main Flask application file.
Handles routing, file uploads, and rendering results.
"""

from flask import Flask, render_template, request
import os

from resume_parser import extract_text_from_pdf, extract_skills
from job_matcher import match_jobs

app = Flask(__name__)

# Folder to store uploaded resumes
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """
    Checks if uploaded file is a PDF.

    Args:
        filename (str): Uploaded file name

    Returns:
        bool: True if PDF, else False
    """
    return '.' in filename and filename.lower().endswith('.pdf')

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main route for resume upload and job recommendation.
    """
    if request.method == "POST":
        file = request.files.get("resume")

        # Validate file presence and type
        if not file or file.filename == "":
            return "No file selected"

        if not allowed_file(file.filename):
            return "Invalid file type. Upload PDF only."

        # Save uploaded resume
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Process resume
        resume_text = extract_text_from_pdf(file_path)
        skills = extract_skills(resume_text)

        # Match jobs based on skills
        jobs = match_jobs(skills)

        return render_template(
            "result.html",
            skills=skills,
            jobs=jobs
        )

    return render_template("index.html")

if __name__ == "__main__":
    # Run Flask app in debug mode
    app.run(debug=True)

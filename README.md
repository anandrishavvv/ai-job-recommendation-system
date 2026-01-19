# AI Job Recommendation System

An AI-powered web application that recommends suitable jobs based on a user's resume.

## 🚀 Features
- PDF resume upload with validation
- Skill extraction using NLP (spaCy)
- Job matching and ranking
- Skill gap analysis
- Clean and responsive UI
- Modular and scalable Flask backend

## 🛠️ Tech Stack
- Python
- Flask
- spaCy (NLP)
- scikit-learn (ML)
- pandas
- HTML & CSS

## 📌 How It Works
1. User uploads a PDF resume
2. System extracts skills using NLP
3. Skills are matched against job requirements
4. Top job recommendations are displayed with missing skills

## 📂 Project Structure
- `app.py` – Main Flask application
- `resume_parser.py` – Resume text & skill extraction
- `job_matcher.py` – Rule-based job matching logic
- `model.py` – ML-based job recommendation model
- `templates/` – HTML templates
- `static/` – CSS files

## 🌍 Deployment
The application can be deployed on platforms like Render or Railway using Gunicorn.

## 🎯 Use Case
Ideal for students, job seekers, and recruiters to analyze resumes and identify suitable job roles.

---

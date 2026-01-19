"""
model.py
--------
This module trains and uses an ML model to recommend jobs
using TF-IDF and cosine similarity.
"""

import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def train_model():
    """
    Trains TF-IDF model on job skills and saves it.
    """
    jobs = pd.read_csv("data/jobs.csv")

    # Convert skill text into numerical vectors
    vectorizer = TfidfVectorizer()
    job_vectors = vectorizer.fit_transform(jobs["required_skills"])

    # Store model components together
    model_data = {
        "vectorizer": vectorizer,
        "job_vectors": job_vectors,
        "jobs": jobs
    }

    # Save trained model
    with open("models/job_model.pkl", "wb") as f:
        pickle.dump(model_data, f)


def predict_jobs(user_skills, top_n=3):
    """
    Predicts best job matches using cosine similarity.

    Args:
        user_skills (list): Extracted resume skills

    Returns:
        DataFrame: Top job matches
    """
    # Load trained model
    with open("models/job_model.pkl", "rb") as f:
        data = pickle.load(f)

    # Convert user skills into vector form
    user_text = " ".join(user_skills)
    user_vector = data["vectorizer"].transform([user_text])

    # Calculate similarity between user and job vectors
    similarity_scores = cosine_similarity(user_vector, data["job_vectors"])[0]

    data["jobs"]["score"] = similarity_scores

    return data["jobs"].sort_values(by="score", ascending=False).head(top_n)

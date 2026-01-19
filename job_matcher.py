"""
job_matcher.py
--------------
This module matches extracted user skills with job requirements.
It calculates match score and identifies skill gaps.
"""

import pandas as pd

def match_jobs(user_skills, top_n=3):
    """
    Matches user skills with job requirements from CSV file.

    Args:
        user_skills (list): Skills extracted from resume
        top_n (int): Number of top jobs to return

    Returns:
        list: Ranked job recommendations
    """
    # Load job dataset
    jobs = pd.read_csv("data/jobs.csv")
    results = []

    for _, row in jobs.iterrows():
        # Convert required skills string to list
        job_skills = [s.strip() for s in row["required_skills"].split(",")]

        # Find overlapping skills
        matched_skills = set(user_skills) & set(job_skills)

        results.append({
            "job_title": row["job_title"],
            "match_score": len(matched_skills),
            "matched_skills": list(matched_skills),
            "missing_skills": list(set(job_skills) - set(user_skills))
        })

    # Sort jobs by match score (descending)
    results.sort(key=lambda x: x["match_score"], reverse=True)

    return results[:top_n]

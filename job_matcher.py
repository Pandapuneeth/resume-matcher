import json

def load_job_descriptions(path='job_descriptions.json'):
    with open(path, 'r') as file:
        return json.load(file)

def match_jobs(resume_skills, job_data):
    scores = {}
    for job, required_skills in job_data.items():
        matched = set(resume_skills) & set(required_skills)
        score = len(matched) / len(required_skills)
        scores[job] = round(score * 100, 2)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserPreferences(BaseModel):
    skills: str
    location: str
    salary_range: tuple

@app.post("/recommend_jobs/")
def recommend_jobs(preferences: UserPreferences):
    # The 'recommend_jobs' function should be implemented here
    recommended_jobs = recommend_jobs(preferences.skills, preferences.location, preferences.salary_range)
    return recommended_jobs[['job_title', 'company', 'location', 'salary']].to_dict()


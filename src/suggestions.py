import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "models/gemini-3-flash-preview"

def generate_suggestions(resume_sections: dict, jd_text: str) -> str:
    prompt = f"""
You are a career assistant.

Given:
- Resume sections (skills, experience, education)
- A job description

Provide 4–6 concise, actionable suggestions on how the candidate can improve
their resume to better match the job.

Rules:
- Do NOT rewrite the resume
- Do NOT mention hiring or rejection
- Focus on missing or weak areas
- Be constructive and neutral
- Bullet points only

Resume sections:
Skills:
{resume_sections.get("skills","")}

Experience:
{resume_sections.get("experience","")}

Education:
{resume_sections.get("education","")}

Job description:
{jd_text}
"""

    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(prompt)
    return response.text

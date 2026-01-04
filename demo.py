import os
from src.parser import extract_text_from_pdf, split_sections
from src.embedding import embed_text, cosine_similarity

RESUME_PATH = "data/resumes/sample.pdf"
JD_PATH = "data/job_descriptions/jd.txt"

def score_resume(resume_path: str, jd_path: str) -> float:
    resume_text = extract_text_from_pdf(resume_path)
    jd_text = open(jd_path, encoding="utf-8").read()

    sections = split_sections(resume_text)

    score = 0.0
    if sections["skills"]:
        score += 0.5 * cosine_similarity(
            embed_text(sections["skills"]),
            embed_text(jd_text)
        )
    if sections["experience"]:
        score += 0.4 * cosine_similarity(
            embed_text(sections["experience"]),
            embed_text(jd_text)
        )
    if sections["education"]:
        score += 0.1 * cosine_similarity(
            embed_text(sections["education"]),
            embed_text(jd_text)
        )

    return round(score, 2)

if __name__ == "__main__":
    if not os.path.exists(RESUME_PATH):
        raise FileNotFoundError(f"Missing resume: {RESUME_PATH}")

    if not os.path.exists(JD_PATH):
        raise FileNotFoundError(f"Missing job description: {JD_PATH}")

    final_score = score_resume(RESUME_PATH, JD_PATH)
    print(f"Resume–JD match score: {final_score}")

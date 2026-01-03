from src.parser import extract_text_from_pdf, split_sections
from src.embedding import embed_text, cosine_similarity

resume_text = extract_text_from_pdf("data/resumes/sample.pdf")
jd_text = open("data/job_descriptions/jd.txt", encoding="utf-8").read()

sections = split_sections(resume_text)

scores = []

if sections["skills"]:
    scores.append(0.5 * cosine_similarity(embed_text(sections["skills"]), embed_text(jd_text)))

if sections["experience"]:
    scores.append(0.4 * cosine_similarity(embed_text(sections["experience"]), embed_text(jd_text)))

if sections["education"]:
    scores.append(0.1 * cosine_similarity(embed_text(sections["education"]), embed_text(jd_text)))

final_score = sum(scores)

print("Weighted match score:", round(final_score, 3))

import os
import streamlit as st
from src.parser import extract_text_from_pdf, split_sections
from src.embedding import embed_text, cosine_similarity
from src.suggestions import generate_suggestions

st.set_page_config(page_title="Resume Screener", layout="centered")
st.title("📄 AI Resume Screener")



# ---- MODE SELECTOR ----
mode = st.radio(
    "Select mode",
    ["Recruiter", "Job Seeker"],
    horizontal=True
)

# =========================
# 👔 RECRUITER MODE
# =========================
if mode == "Recruiter":
    st.subheader("Recruiter View")

    jd_file = st.file_uploader("Upload Job Description (TXT)", type=["txt"])
    resume_files = st.file_uploader(
        "Upload Resume PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if jd_file and resume_files:
        jd_text = jd_file.read().decode("utf-8")
        results = []

        for resume in resume_files:
            temp_path = f"temp_{resume.name}"
            with open(temp_path, "wb") as f:
                f.write(resume.getbuffer())

            resume_text = extract_text_from_pdf(temp_path)
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

            results.append((resume.name, round(score, 2)))
            os.remove(temp_path)

        results.sort(key=lambda x: x[1], reverse=True)

        st.subheader("📊 Ranked Candidates")
        for i, (name, score) in enumerate(results, start=1):
            st.write(f"**{i}. {name}** — {score}")

# =========================
# 🙋 JOB SEEKER MODE
# =========================
if mode == "Job Seeker":
    st.subheader("Job Seeker View")

    resume_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])
    jd_file = st.file_uploader("Upload Job Description (TXT)", type=["txt"])

    sections = None
    jd_text = None
    score = None

    if resume_file and jd_file:
        jd_text = jd_file.read().decode("utf-8")

        temp_path = f"temp_{resume_file.name}"
        with open(temp_path, "wb") as f:
            f.write(resume_file.getbuffer())

        resume_text = extract_text_from_pdf(temp_path)
        sections = split_sections(resume_text)
        os.remove(temp_path)

        score = 0.0
        breakdown = {}

        if sections["skills"]:
            s = cosine_similarity(embed_text(sections["skills"]), embed_text(jd_text))
            breakdown["Skills"] = round(s, 2)
            score += 0.5 * s

        if sections["experience"]:
            e = cosine_similarity(embed_text(sections["experience"]), embed_text(jd_text))
            breakdown["Experience"] = round(e, 2)
            score += 0.4 * e

        if sections["education"]:
            ed = cosine_similarity(embed_text(sections["education"]), embed_text(jd_text))
            breakdown["Education"] = round(ed, 2)
            score += 0.1 * ed

        st.metric("Estimated Role Fit", round(score, 2))

        st.subheader("📌 Score Breakdown")
        for k, v in breakdown.items():
            st.write(f"- **{k}**: {v}")

    # ---- AI SUGGESTIONS TOGGLE (SAFE) ----
    show_suggestions = st.checkbox(
        "Show improvement suggestions (AI)",
        disabled=not (resume_file and jd_file)
    )

    if show_suggestions and sections and jd_text:
        with st.spinner("Generating suggestions..."):
            tips = generate_suggestions(sections, jd_text)

        st.subheader("🛠️ Suggestions to strengthen your resume")
        st.write(tips)

    elif show_suggestions:
        st.info("Upload a resume and job description to see suggestions.")

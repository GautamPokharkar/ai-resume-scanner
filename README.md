# 📄 AI Resume Screener – Semantic Matching Application

An **AI-assisted resume screening application** designed to evaluate **semantic alignment** between resumes and job descriptions using **embedding-based similarity scoring**.  
The system supports **role-based usage** for recruiters and job seekers, enabling candidate ranking, resume self-evaluation, and targeted improvement suggestions.

---

## ✅ Key Features

- Role-based modes for **Recruiters** and **Job Seekers**
- Semantic resume–job description matching using embeddings
- Weighted scoring across resume sections (**skills, experience, education**)
- Multi-resume upload and ranking for recruiter workflows
- Resume self-assessment with improvement suggestions for job seekers
- Optional AI-generated guidance with user-controlled toggle
- Interactive web interface built with Streamlit

---

## 🖥️ Application Overview

- Built as a **single-page interactive application**
- Supports **PDF resume uploads** and text-based job descriptions
- Real-time scoring and ranking using deterministic logic
- Clean separation between scoring logic and AI-generated explanations
- Designed for learning and experimentation rather than automated hiring

---

## 🧠 System Design Highlights

- **Deterministic scoring core** using cosine similarity for reproducibility
- Section-aware evaluation to reflect real-world hiring priorities
- LLMs used only for **explanations and suggestions**, not scoring decisions
- Shared core logic with **role-specific user interfaces**
- Emphasis on transparency, explainability, and responsible AI usage

---

## 🧰 Tech Stack

### Frontend / UI
- Streamlit

### Backend / Core Logic
- Python
- Google Gemini API (Embeddings and Text Generation)
- NumPy

### Utilities
- PyMuPDF (PDF text extraction)
- python-dotenv (environment configuration)

---

## 🎯 Learning Outcomes

- Designed an **AI-assisted system** with deterministic semantic scoring
- Implemented resume–job matching using **embeddings and cosine similarity**
- Built role-based user experiences on top of a shared scoring engine
- Applied responsible AI principles by separating scoring and explanation
- Gained experience building **interactive ML-powered applications**

---


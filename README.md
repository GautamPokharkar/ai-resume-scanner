# 📄 AI Resume Enhancer – Semantic Matching & Feedback Application

An **AI-powered resume enhancement application** designed to analyze, parse, and measure **semantic alignment** between resumes and job descriptions using **embedding-based similarity scoring**.  
The system supports **role-based usage** for recruiters and job seekers, enabling candidate ranking, resume self-evaluation, and targeted improvement suggestions.

---

## ✅ Key Features

- Role-based modes for **Recruiters** and **Job Seekers**
- Semantic resume–job description matching using embeddings
- Weighted scoring across resume sections (**skills, experience, education**)
- Multi-resume upload and ranking for recruiter workflows
- Resume self-assessment with actionable improvement suggestions
- Optional AI-generated guidance with user-controlled toggle
- Interactive web interface built with Streamlit

---

## 🖥️ Application Overview

- Built as a **single-page interactive application**
- Supports **PDF resume uploads** and text-based job descriptions
- Real-time similarity scoring using deterministic logic
- Clear separation between scoring logic and AI-generated feedback
- Designed for learning, analysis, and resume improvement (not hiring decisions)

---

## 🧠 System Design Highlights

- **Deterministic scoring core** using cosine similarity for reproducibility
- Section-aware evaluation to reflect real-world hiring priorities
- LLMs used only for **explanations and improvement suggestions**, not scoring
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

- Designed an **AI-powered system** with deterministic semantic matching
- Implemented resume–job alignment using **embeddings and cosine similarity**
- Built role-based user experiences on a shared scoring engine
- Applied responsible AI principles by separating scoring and explanation
- Gained experience building **interactive NLP-powered applications**

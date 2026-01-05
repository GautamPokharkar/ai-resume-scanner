📄 AI Resume Screener – Semantic Matching Application

An AI-assisted resume screening application designed to evaluate semantic alignment between resumes and job descriptions using deterministic embedding-based scoring.
The system supports role-based usage for recruiters and job seekers, providing ranking, similarity scores, and targeted improvement suggestions.

✅ Key Features

Role-based modes for Recruiters and Job Seekers

Semantic resume–job description matching using embeddings

Weighted scoring across resume sections (skills, experience, education)

Multi-resume ranking for recruiter workflows

Resume self-evaluation and improvement suggestions for job seekers

Optional AI-generated guidance with user-controlled toggle

Interactive web interface built with Streamlit

🖥️ Application Overview

Built as a single-page interactive application

Supports PDF resume uploads and text-based job descriptions

Provides real-time scoring and ranking

Clear separation between deterministic scoring and AI explanations

🧠 System Design Highlights

Deterministic scoring using cosine similarity for reproducibility

Section-aware evaluation to reflect real hiring priorities

LLMs used only for explanations, not scoring decisions

Shared core logic with role-specific user interfaces

Safe handling of user inputs and optional AI usage

🧰 Tech Stack

Frontend / UI

Streamlit

Backend / Core Logic

Python

Google Gemini API (Embeddings + Text Generation)

NumPy

Utilities

PyMuPDF (PDF text extraction)

dotenv (environment configuration)

🎯 Learning Outcomes

Designed an AI-assisted system with deterministic core logic

Implemented semantic matching using embeddings and cosine similarity

Built role-based user experiences on top of a shared scoring engine

Applied responsible AI principles by separating scoring and explanation

Gained experience building interactive ML-powered applications

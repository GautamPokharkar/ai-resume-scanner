import os
import numpy as np
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

EMBED_MODEL = "models/text-embedding-004"

def embed_text(text: str) -> np.ndarray:
    res = genai.embed_content(
        model=EMBED_MODEL,
        content=text
    )
    return np.array(res["embedding"])

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return float(
        np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    )

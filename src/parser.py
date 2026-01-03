import fitz  # PyMuPDF

def extract_text_from_pdf(path: str) -> str:
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)

def split_sections(text: str) -> dict:
    text = text.lower()
    sections = {
        "skills": "",
        "experience": "",
        "education": ""
    }

    current = None
    for line in text.splitlines():
        if "skill" in line:
            current = "skills"
        elif "experience" in line:
            current = "experience"
        elif "education" in line:
            current = "education"
        elif current:
            sections[current] += line + " "

    return sections

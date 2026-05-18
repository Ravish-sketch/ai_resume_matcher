import fitz # PyMuPDF
import pdfplumber
from src.utils.text_cleaner import clean_text

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extracts text from a given PDF file using PyMuPDF and falls back to pdfplumber."""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        doc.close()
    except Exception as e:
        # Fallback to pdfplumber
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + "\n"
        except Exception as e2:
            pass
    
    return clean_text(text)

from src.parser.pdf_loader import extract_text_from_pdf

def parse_resume(file_path: str) -> str:
    """Parses a resume file and extracts clean text."""
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    # Add support for docx here if needed
    return ""

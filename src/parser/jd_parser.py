from src.parser.pdf_loader import extract_text_from_pdf
from src.utils.text_cleaner import clean_text

def parse_jd(input_data: str, is_file: bool = False) -> str:
    """Parses Job Description from raw text or a file."""
    if is_file:
        if input_data.endswith('.pdf'):
            return extract_text_from_pdf(input_data)
        return ""
    else:
        return clean_text(input_data)

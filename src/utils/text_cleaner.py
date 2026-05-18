import re

def clean_text(text: str) -> str:
    """Cleans up extracted text by removing extra spaces and special chars."""
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

import google.generativeai as genai
from src.config.settings import GEMINI_API_KEY
import json

# Configure Gemini
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def extract_skills_with_llm(text: str) -> list:
    """Uses Gemini to extract skills from text."""
    if not GEMINI_API_KEY or not text:
        import re
        words = re.findall(r'\b[A-Za-z]+\b', text)
        skills = [w for w in words if w.lower() in ['python', 'java', 'react', 'sql', 'aws', 'docker', 'machine learning', 'ai', 'css', 'html', 'javascript', 'pandas', 'numpy']]
        return list(set(skills))
        
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = f"Extract a list of professional skills, technologies, and tools from the following text. Return ONLY a JSON list of strings, nothing else. Text: {text}"
        response = model.generate_content(prompt)
        content = response.text.strip()
        if content.startswith("```json"):
            content = content[7:-3]
        elif content.startswith("```"):
            content = content[3:-3]
        skills = json.loads(content)
        return list(set(skills))
    except Exception as e:
        print(f"Error extracting skills: {e}")
        return []

def analyze_resume_against_jd(resume_text: str, jd_text: str) -> dict:
    """Uses Gemini to get a detailed analysis."""
    if not GEMINI_API_KEY or not resume_text or not jd_text:
        return {
            "suggestions": ["Add more keywords related to Cloud Computing", "Highlight leadership experience"],
            "ats_feedback": "Your resume format is readable but could use more quantifiable metrics.",
            "missing_skills": ["Docker", "Kubernetes"]
        }
        
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = f"""
        Analyze the following resume against the job description.
        Resume: {resume_text}
        
        Job Description: {jd_text}
        
        Provide your analysis strictly in the following JSON format. Do not use a markdown codeblock, just return raw JSON:
        {{
            "suggestions": ["suggestion 1", "suggestion 2"],
            "ats_feedback": "overall feedback on formatting and ATS parsability",
            "missing_skills": ["skill 1", "skill 2"]
        }}
        """
        response = model.generate_content(prompt)
        content = response.text.strip()
        if content.startswith("```json"):
            content = content[7:-3]
        elif content.startswith("```"):
            content = content[3:-3]
        
        analysis = json.loads(content)
        return analysis
    except Exception as e:
        print(f"Error analyzing resume: {e}")
        return {
            "suggestions": [f"API Error: {str(e)}"],
            "ats_feedback": "N/A",
            "missing_skills": []
        }

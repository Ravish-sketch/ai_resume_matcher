from src.ai.embeddings import get_embedding, get_similarity
from src.ai.llm_engine import extract_skills_with_llm

def calculate_match_score(resume_text: str, jd_text: str) -> dict:
    """Calculates match score between resume and JD."""
    resume_emb = get_embedding(resume_text)
    jd_emb = get_embedding(jd_text)
    
    semantic_score = get_similarity(resume_emb, jd_emb)
    
    resume_skills = extract_skills_with_llm(resume_text)
    jd_skills = extract_skills_with_llm(jd_text)
    
    matched_skills = set(resume_skills).intersection(set(jd_skills))
    skill_score = len(matched_skills) / len(jd_skills) if len(jd_skills) > 0 else 0
    
    # Combined score
    overall_score = (semantic_score * 0.6) + (skill_score * 0.4)
    
    return {
        "match_percentage": round(overall_score * 100, 2),
        "semantic_similarity": round(semantic_score * 100, 2),
        "skill_coverage": round(skill_score * 100, 2),
        "matched_skills": list(matched_skills),
        "resume_skills": resume_skills,
        "jd_skills": jd_skills
    }

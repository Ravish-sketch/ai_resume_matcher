import streamlit as st
import os

from src.ui.sidebar import render_sidebar
from src.ui.dashboard import render_dashboard
from src.parser.resume_parser import parse_resume
from src.parser.jd_parser import parse_jd
from src.ai.matcher import calculate_match_score
from src.ai.llm_engine import analyze_resume_against_jd

st.set_page_config(page_title="AI Resume Matcher", page_icon="🚀", layout="wide")

# Apply custom CSS
st.markdown("""
<style>
    /* Global Styles & Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif !important;
    }
    
    .stApp {
        background-color: #0B0F19;
        background-image: 
            radial-gradient(circle at 15% 50%, rgba(59, 130, 246, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 85% 30%, rgba(139, 92, 246, 0.08) 0%, transparent 50%);
    }
    
    /* Headers & Text */
    h1, h2, h3 {
        color: #F8FAFC !important;
        font-weight: 600 !important;
    }
    
    h1 {
        background: linear-gradient(90deg, #3B82F6, #8B5CF6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px !important;
    }

    /* Metric Cards Premium Design */
    .metric-card {
        padding: 24px; 
        border-radius: 16px; 
        background: rgba(30, 41, 59, 0.4); 
        border: 1px solid rgba(255, 255, 255, 0.05); 
        margin-bottom: 24px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.15);
        border-color: rgba(59, 130, 246, 0.4);
    }
    .metric-card h3 {
        margin: 0; 
        color: #94A3B8 !important; 
        font-size: 14px !important;
        font-weight: 400 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .metric-card h2 {
        margin: 10px 0 0 0; 
        color: #F8FAFC !important; 
        font-size: 36px !important;
        font-weight: 700 !important;
    }
    .metric-card p {
        margin: 8px 0 0 0; 
        color: #3B82F6 !important; 
        font-size: 13px !important;
        opacity: 0.8;
    }
    
    /* Missing Skills items */
    .missing-skill {
        background: rgba(239, 68, 68, 0.1);
        border-left: 4px solid #EF4444;
        padding: 10px 15px;
        margin-bottom: 8px;
        border-radius: 4px;
        color: #F8FAFC;
    }
    
    /* Streamlit Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(30, 41, 59, 0.5);
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
        color: #94A3B8;
        border: 1px solid rgba(255,255,255,0.05);
        border-bottom: none;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(59, 130, 246, 0.2) !important;
        color: #3B82F6 !important;
        border-bottom: 2px solid #3B82F6 !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #111827 !important;
        border-right: 1px solid rgba(255,255,255,0.05);
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #3B82F6, #8B5CF6);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        transition: opacity 0.3s;
    }
    .stButton>button:hover {
        opacity: 0.9;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def main():
    resume_path, jd_text_input, jd_file_path, analyze_btn = render_sidebar()
    
    if not analyze_btn:
        st.info("👈 Please upload a resume and job description from the sidebar and click 'Analyze Match'.")
        return
        
    if not resume_path:
        st.error("Please upload a resume.")
        return
        
    if not jd_text_input and not jd_file_path:
        st.error("Please provide a Job Description.")
        return
        
    with st.spinner("Analyzing Resume against Job Description..."):
        # 1. Parse Resume
        resume_text = parse_resume(resume_path)
        
        # 2. Parse JD
        if jd_file_path:
            jd_text = parse_jd(jd_file_path, is_file=True)
        else:
            jd_text = parse_jd(jd_text_input, is_file=False)
            
        if not resume_text:
            st.error("Could not extract text from the resume. Please check the file.")
            return
            
        if not jd_text:
            st.error("Could not extract text from the JD. Please check the input.")
            return
            
        # 3. Calculate Scores
        match_results = calculate_match_score(resume_text, jd_text)
        
        # 4. Get AI Analysis
        ai_analysis = analyze_resume_against_jd(resume_text, jd_text)
        
        # 5. Render Dashboard
        render_dashboard(match_results, ai_analysis)

if __name__ == "__main__":
    main()

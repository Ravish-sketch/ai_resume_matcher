import streamlit as st
import os
from src.config.settings import RESUMES_DIR, JD_DIR

def render_sidebar():
    st.sidebar.markdown('<h1 style="background: linear-gradient(90deg, #3B82F6, #8B5CF6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">🚀 Resume Matcher</h1>', unsafe_allow_html=True)
    
    st.sidebar.header("1. Upload Resume")
    resume_file = st.sidebar.file_uploader("Upload PDF/DOCX", type=["pdf", "docx"], key="resume")
    
    st.sidebar.header("2. Job Description")
    jd_input_type = st.sidebar.radio("JD Input Method", ["Paste Text", "Upload File"])
    
    jd_text = ""
    jd_file = None
    if jd_input_type == "Paste Text":
        jd_text = st.sidebar.text_area("Paste JD Here", height=150)
    else:
        jd_file = st.sidebar.file_uploader("Upload JD File", type=["pdf", "txt"], key="jd")
        
    analyze_btn = st.sidebar.button("Analyze Match 🚀", use_container_width=True)
    
    # Save uploaded files temporarily
    resume_path = None
    jd_path = None
    
    if resume_file:
        os.makedirs(RESUMES_DIR, exist_ok=True)
        resume_path = os.path.join(RESUMES_DIR, resume_file.name)
        with open(resume_path, "wb") as f:
            f.write(resume_file.getbuffer())
            
    if jd_file:
        os.makedirs(JD_DIR, exist_ok=True)
        jd_path = os.path.join(JD_DIR, jd_file.name)
        with open(jd_path, "wb") as f:
            f.write(jd_file.getbuffer())
            
    return resume_path, jd_text, jd_path, analyze_btn

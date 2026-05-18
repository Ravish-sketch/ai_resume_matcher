import streamlit as st
from src.ui.components import render_metric_card
import pandas as pd
import plotly.express as px

def render_dashboard(match_results: dict, ai_analysis: dict):
    st.title("📊 Analysis Dashboard")
    
    # Top Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        render_metric_card("Overall Match Score", f"{match_results['match_percentage']}%", "Combined semantic and skill score")
    with col2:
        render_metric_card("Skill Coverage", f"{match_results['skill_coverage']}%", "Keywords found in resume")
    with col3:
        render_metric_card("Semantic Similarity", f"{match_results['semantic_similarity']}%", "Contextual alignment")
        
    st.markdown("---")
    
    # Charts and Details
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Skill Gap Analysis")
        # Creating a simple dataframe for skills
        all_skills = list(set(match_results['jd_skills'] + match_results['resume_skills']))
        skill_data = []
        for skill in all_skills:
            if skill in match_results['jd_skills'] and skill in match_results['resume_skills']:
                status = "Matched"
            elif skill in match_results['jd_skills']:
                status = "Missing"
            else:
                status = "Extra in Resume"
            skill_data.append({"Skill": skill, "Status": status})
            
        if skill_data:
            df = pd.DataFrame(skill_data)
            fig = px.pie(df, names='Status', title='Skill Match Distribution', hole=0.4, color='Status', 
                         color_discrete_map={"Matched": "#10B981", "Missing": "#EF4444", "Extra in Resume": "#3B82F6"})
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No explicit skills extracted. Showing semantic match only.")
            
    with col2:
        st.subheader("Missing Skills")
        missing_skills = [s for s in match_results['jd_skills'] if s not in match_results['resume_skills']]
        if missing_skills:
            for skill in missing_skills:
                st.markdown(f'<div class="missing-skill">❌ {skill}</div>', unsafe_allow_html=True)
        elif ai_analysis.get('missing_skills'):
            for skill in ai_analysis.get('missing_skills'):
                st.markdown(f'<div class="missing-skill">❌ {skill}</div>', unsafe_allow_html=True)
        else:
            st.success("No critical missing skills found!")
            
    st.markdown("---")
    
    st.subheader("💡 AI Suggestions for Improvement")
    
    tabs = st.tabs(["✨ Resume Tweaks", "🤖 ATS Feedback"])
    with tabs[0]:
        st.markdown("<br>", unsafe_allow_html=True)
        for suggestion in ai_analysis.get("suggestions", []):
            st.info(suggestion)
    with tabs[1]:
        st.markdown("<br>", unsafe_allow_html=True)
        st.warning(ai_analysis.get("ats_feedback", "N/A"))

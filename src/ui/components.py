import streamlit as st

def render_metric_card(title: str, value: str, description: str = ""):
    st.markdown(f"""
        <div class="metric-card">
            <h3>{title}</h3>
            <h2>{value}</h2>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)

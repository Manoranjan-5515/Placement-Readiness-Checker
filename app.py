import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Placement Readiness Checker",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #2c3e50; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stProgress > div > div > div > div { background-color: #27ae60; }
    </style>
    """, unsafe_allow_html=True)

def generate_radar_chart(skills_dict):
    """Generates a professional radar chart for skill visualization."""
    categories = list(skills_dict.keys())
    values = list(skills_dict.values())
    
    # Close the polygon
    categories.append(categories[0])
    values.append(values[0])

    fig = go.Figure(data=go.Scatterpolar(
      r=values,
      theta=categories,
      fill='toself',
      fillcolor='rgba(41, 128, 185, 0.4)',
      line=dict(color='#2980b9', width=2),
      name='Student Profile'
    ))

    fig.update_layout(
      polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
      showlegend=False,
      margin=dict(l=40, r=40, t=20, b=20)
    )
    return fig

def main():
    st.title("🎓 Smart Placement Readiness Checker")
    st.markdown("Analyze your academic and technical profile to predict your placement probability and identify areas for improvement.")

    # --- SIDEBAR: USER INPUTS ---
    with st.sidebar:
        st.header("📊 Student Profile Data")
        cgpa = st.slider("CGPA", 0.0, 10.0, 7.5, 0.1)
        coding_skill = st.slider("Coding & DSA (1-10)", 1, 10, 6)
        core_subjects = st.slider("Core Subjects (OS, DBMS, CN) (1-10)", 1, 10, 7)
        comm_skill = st.slider("Communication Skills (1-10)", 1, 10, 6)
        internships = st.number_input("Number of Internships", 0, 5, 1)
        projects = st.number_input("Major Projects", 0, 10, 2)
        
        analyze_btn = st.button("Analyze Readiness", type="primary", use_container_width=True)

    # --- MAIN CONTENT AREA ---
    if analyze_btn:
        with st.spinner("Analyzing profile metrics..."):
            time.sleep(1.2) # Simulate model processing time
            
            # Simulated readiness calculation logic
            base_score = (cgpa / 10) * 30 + (coding_skill / 10) * 25 + (core_subjects / 10) * 15 + (comm_skill / 10) * 15
            bonus_score = min(internships * 5 + projects * 3, 15)
            readiness_score = min(base_score + bonus_score, 100)

            # Display Results in Columns
            col1, col2 = st.columns([1, 1.5])
            
            with col1:
                st.subheader("Placement Probability")
                st.metric(label="Readiness Index", value=f"{readiness_score:.1f}%", delta=f"{readiness_score - 75:.1f}% vs Average")
                st.progress(int(readiness_score))
                
                if readiness_score > 80:
                    st.success("Excellent profile! You are highly prepared for Tier-1 company placements.")
                elif readiness_score > 60:
                    st.info("Good profile. Focus on strengthening your weaker areas to improve your chances.")
                else:
                    st.warning("Needs improvement. Consider building more projects and practicing DSA.")

            with col2:
                st.subheader("Skill Distribution")
                skills_data = {
                    "Academics (CGPA)": cgpa,
                    "Coding & DSA": coding_skill,
                    "Core Subjects": core_subjects,
                    "Communication": comm_skill,
                    "Practical Exp": min(internships * 2.5 + projects * 1.5, 10)
                }
                fig = generate_radar_chart(skills_data)
                st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
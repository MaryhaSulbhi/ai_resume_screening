

import streamlit as st
import pandas as pd
from llm_engine import analyze_resume_llm

from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from ranking_engine import compute_similarity
from utils import calculate_ats_score
from feedback_engine import generate_feedback
from question_generator import generate_questions

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Screening System",
    layout="wide",
    page_icon="🤖"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
    }
    .card {
        padding: 15px;
        border-radius: 12px;
        background-color: #1e1e1e;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🤖 AI Resume Screener")
page = st.sidebar.radio("Navigate", [
    "🏠 Home",
    "📂 Upload & Analyze",
    "📊 Results"
])

# ---------------- SESSION STORAGE ----------------
if "df" not in st.session_state:
    st.session_state["df"] = None

if "job_description" not in st.session_state:
    st.session_state["job_description"] = ""

# ---------------- HOME PAGE ----------------
if page == "🏠 Home":
    st.markdown('<p class="main-title">🚀 AI Resume Screening System</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("📄 Resumes", "Multiple Upload")
    col2.metric("🤖 AI Analysis", "Enabled")
    col3.metric("📊 Ranking", "Smart ATS")

    st.markdown("---")

    st.subheader("✨ Features")
    st.write("""
    - Resume Parsing 📄  
    - Skill Extraction 🧠  
    - ATS Score Calculation 🎯  
    - AI Hiring Decision 🤖  
    - Interview Questions 🎤  
    - Feedback System 💡  
    """)

# ---------------- UPLOAD PAGE ----------------
elif page == "📂 Upload & Analyze":
    st.title("📂 Upload & Analyze Resumes")

    job_description = st.text_area("📌 Enter Job Description")

    uploaded_files = st.file_uploader(
        "📄 Upload Resume PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("🚀 Analyze Candidates"):

        if job_description == "":
            st.warning("⚠️ Please enter a job description")

        elif uploaded_files:

            results = []

            with st.spinner("⏳ Processing resumes..."):

                for file in uploaded_files:

                    resume_text = extract_text_from_pdf(file)
                    llm_analysis = analyze_resume_llm(resume_text, job_description)

                    skills = extract_skills(resume_text)
                    similarity = compute_similarity(resume_text, job_description)

                    job_skills = extract_skills(job_description)
                    skill_match = len(set(skills).intersection(job_skills)) / (len(job_skills) + 1)

                    ats_score = calculate_ats_score(similarity, skill_match)

                    feedback = generate_feedback(skills, job_skills)
                    questions = generate_questions(skills)

                    results.append({
                        "Candidate": file.name,
                        "ATS Score": round(ats_score, 2),
                        "Similarity (%)": round(similarity * 100, 2),
                        "Skills": ", ".join(skills),
                        "Feedback": feedback,
                        "Questions": "\n".join(questions),
                        "LLM Analysis": llm_analysis
                    })

            df = pd.DataFrame(results)
            df = df.sort_values(by="ATS Score", ascending=False)

            # Store in session
            st.session_state["df"] = df
            st.session_state["job_description"] = job_description

            st.success("✅ Analysis Complete! Go to Results tab")

        else:
            st.warning("⚠️ Please upload at least one resume")

# ---------------- RESULTS PAGE ----------------
elif page == "📊 Results":
    st.title("📊 Candidate Analysis")

    df = st.session_state.get("df")

    if df is None:
        st.warning("⚠️ No results yet. Please analyze resumes first.")
    else:
        # 🏆 Top Candidate
        st.success(f"🏆 Top Candidate: {df.iloc[0]['Candidate']}")

        # 📊 Chart
        st.subheader("📊 ATS Score Distribution")
        st.bar_chart(df.set_index("Candidate")["ATS Score"])

        st.markdown("---")

        # 👤 Candidate Cards
        for i, row in df.iterrows():

            with st.container():
                col1, col2 = st.columns([2, 1])

                # LEFT SIDE
                with col1:
                    st.subheader(f"👤 {row['Candidate']}")
                    st.write("🛠 Skills:", row["Skills"])

                # RIGHT SIDE
                with col2:
                    st.metric("🎯 ATS Score", f"{row['ATS Score']}")
                    st.metric("📊 Similarity", f"{row['Similarity (%)']}%")
                    st.progress(row["ATS Score"] / 100)

                # EXPANDERS
                with st.expander("🤖 AI Hiring Decision"):
                    st.write(row["LLM Analysis"])

                with st.expander("💡 Feedback"):
                    st.write(row["Feedback"])

                with st.expander("🎤 Interview Questions"):
                    st.write(row["Questions"])

                st.markdown("---")


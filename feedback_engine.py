def generate_feedback(resume_skills, job_skills):

    missing_skills = list(set(job_skills) - set(resume_skills))

    feedback = []

    if missing_skills:
        feedback.append(f"❌ Missing Skills: {', '.join(missing_skills)}")
    else:
        feedback.append("✅ All required skills present")

    if len(resume_skills) < 5:
        feedback.append("⚠️ Add more relevant skills to strengthen your resume")

    feedback.append("📄 Ensure your resume has clear project descriptions")
    feedback.append("📊 Add measurable achievements (e.g., improved accuracy by 20%)")

    return "\n".join(feedback)
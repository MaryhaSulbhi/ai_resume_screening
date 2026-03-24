import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume_llm(resume_text, job_description):

    prompt = f"""
You are an AI recruiter.

Analyze the candidate resume against the job description.

Return:
1. Short summary of candidate
2. Strengths
3. Weaknesses
4. Final decision (Selected / Rejected)
5. Reason for decision

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
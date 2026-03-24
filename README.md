# 🤖 AI Resume Screening System

🚀 An intelligent web application that automates resume screening using AI, helping recruiters analyze, rank, and evaluate candidates efficiently.

---

## 📌 Overview

The **AI Resume Screening System** is a Streamlit-based application that allows users to:

* Upload multiple resumes (PDF)
* Compare them against a job description
* Extract skills automatically
* Generate ATS scores
* Get AI-based hiring decisions
* Receive feedback and interview questions

This project simulates a **real-world hiring pipeline** using AI and NLP techniques.

---

## ✨ Features

✅ Resume Parsing (PDF)
✅ Skill Extraction using NLP
✅ ATS Score Calculation
✅ Resume–Job Similarity Matching
✅ AI-based Hiring Decision (LLM)
✅ Auto-generated Interview Questions
✅ Feedback System for Candidates
✅ Clean and Interactive UI

---

## 🧠 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **AI/ML:** Sentence Transformers, LLM (Groq API)
* **Libraries:**

  * pandas
  * matplotlib
  * scikit-learn
  * PyPDF2 / pdfplumber
  * python-dotenv

---

## 📂 Project Structure

```
ai_resume_screening/
│── app.py
│── llm_engine.py
│── resume_parser.py
│── skill_extractor.py
│── ranking_engine.py
│── feedback_engine.py
│── question_generator.py
│── utils.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-screening.git
cd ai-resume-screening
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Setup API Key (IMPORTANT)

Create a folder:

```
.streamlit/
```

Inside it, create:

```
secrets.toml
```

Add your API key:

```toml
GROQ_API_KEY = "your_api_key_here"
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 📊 How It Works

1. Enter a **Job Description**
2. Upload multiple **resume PDFs**
3. System performs:

   * Text extraction
   * Skill detection
   * Similarity calculation
   * ATS scoring
4. View:

   * Ranked candidates
   * AI hiring decisions
   * Feedback & interview questions

---


## 🚀 Future Improvements

* 🔐 User Authentication System
* 📄 Downloadable Candidate Reports (PDF)
* 🌍 Shareable Result Links
* 📊 Advanced Analytics Dashboard
* 🧠 GPT-powered Candidate Summary

---

## 👩‍💻 Author

**Maryha Sulbhi**

---

## 📜 License

This project is for educational and portfolio purposes.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

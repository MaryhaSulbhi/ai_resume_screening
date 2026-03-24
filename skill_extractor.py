import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python","machine learning","deep learning","sql","tableau",
    "power bi","data analysis","nlp","pandas","numpy",
    "scikit-learn","tensorflow","pytorch","excel","statistics",
    "streamlit","react","mongodb","postgresql","java","c++"
]

def extract_skills(text):

    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))
    
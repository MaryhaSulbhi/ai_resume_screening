def generate_questions(skills):

    questions = []

    for skill in skills:

        if skill == "python":
            questions.append("Explain Python decorators with an example.")

        elif skill == "machine learning":
            questions.append("Explain bias-variance tradeoff.")

        elif skill == "sql":
            questions.append("What is the difference between JOIN and UNION?")

        elif skill == "data analysis":
            questions.append("How do you handle missing data?")

        elif skill == "nlp":
            questions.append("What is tokenization in NLP?")

    return questions[:5]
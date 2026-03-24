# def calculate_final_score(similarity, skill_match):

#     similarity_weight = 0.7
#     skill_weight = 0.3

#     score = (similarity * similarity_weight) + (skill_match * skill_weight)

#     return round(score * 100,2)

def calculate_ats_score(similarity, skill_match, experience_score=0.5):

    # weights similar to real ATS systems
    similarity_weight = 0.5
    skill_weight = 0.3
    experience_weight = 0.2

    score = (
        similarity * similarity_weight +
        skill_match * skill_weight +
        experience_score * experience_weight
    )

    return round(score * 100, 2)
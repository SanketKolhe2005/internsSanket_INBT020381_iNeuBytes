import pandas as pd

skills_df = pd.read_csv("skills.csv")

ALL_SKILLS = skills_df["Skill"].tolist()


def extract_skills(text):

    text = text.lower()

    found = []

    for skill in ALL_SKILLS:

        if skill.lower() in text:
            found.append(skill)

    return sorted(list(set(found)))


def calculate_ats(found_skills):

    total = len(ALL_SKILLS)

    score = (len(found_skills) / total) * 100

    return round(score, 2)


def missing_skills(found):

    missing = []

    for skill in ALL_SKILLS:

        if skill not in found:
            missing.append(skill)

    return missing
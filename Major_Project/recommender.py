import pandas as pd

jobs = pd.read_csv("job_roles.csv")


def recommend_jobs(skills):

    recommendations = []

    user = [s.lower() for s in skills]

    for _, row in jobs.iterrows():

        required = [x.strip().lower() for x in row["Skills"].split(",")]

        matches = len(set(user) & set(required))

        if matches >= 2:
            recommendations.append(row["Role"])

    return recommendations
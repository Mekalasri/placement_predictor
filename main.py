import pandas as pd
import random
import os

# Ensure data folder exists
if not os.path.exists("data"):
    os.makedirs("data")

data = []

for _ in range(200):
    gpa = round(random.uniform(5.0, 9.8), 2)
    coding_score = random.randint(40, 100)
    internship = random.randint(0, 1)
    projects = random.randint(0, 5)
    communication = round(random.uniform(4.0, 9.5), 2)

    # Simple placement logic
    placement_score = (
        gpa * 5 +
        coding_score * 0.3 +
        internship * 10 +
        projects * 2 +
        communication * 3
    )

    placed = 1 if placement_score > 75 else 0

    data.append([
        gpa,
        coding_score,
        internship,
        projects,
        communication,
        placed
    ])

columns = [
    "GPA",
    "Coding_Score",
    "Internship",
    "Projects",
    "Communication_Score",
    "Placed"
]

df = pd.DataFrame(data, columns=columns)
df.to_csv("data/student_data.csv", index=False)

print("✅ Dataset created successfully inside data folder!")
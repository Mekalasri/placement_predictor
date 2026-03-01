import pandas as pd
import joblib

def get_valid_input(prompt, min_val, max_val, is_int=False):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return int(value) if is_int else value
            else:
                print(f"⚠️ Please enter a value between {min_val} and {max_val}")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

print("📌 ENTER STUDENT DETAILS FOR PREDICTION")

gpa = get_valid_input("GPA (0–10): ", 0, 10)
coding_score = get_valid_input("Coding Score (0–100): ", 0, 100)
internship = get_valid_input("Internship (1 = Yes, 0 = No): ", 0, 1, is_int=True)
projects = get_valid_input("Number of Projects (0–5): ", 0, 5, is_int=True)
communication = get_valid_input("Communication Score (0–10): ", 0, 10)

input_data = pd.DataFrame([[
    gpa,
    coding_score,
    internship,
    projects,
    communication
]], columns=[
    "GPA",
    "Coding_Score",
    "Internship",
    "Projects",
    "Communication_Score"
])

# Load trained model
model = joblib.load("model/placement_model.pkl")

# Predict
prediction = model.predict(input_data)[0]
probability = model.predict_proba(input_data)[0][1]  # Probability of placement

print("\n📊 Prediction Result:")

if prediction == 1:
    print("🎉 HIGH probability of placement")
else:
    print("⚠️ LOW probability of placement")

print(f"📈 Placement Probability: {round(probability * 100, 2)}%")

# Confidence level
if probability > 0.8:
    print("🔎 Strong confidence in prediction.")
elif probability > 0.6:
    print("🔎 Moderate confidence in prediction.")
else:
    print("🔎 Low confidence in prediction.")
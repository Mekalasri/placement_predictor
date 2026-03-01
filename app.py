from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model/placement_model.pkl")

@app.route("/")
def home():
    return "Placement Probability Predictor API is running."

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    input_data = pd.DataFrame([[
        data["GPA"],
        data["Coding_Score"],
        data["Internship"],
        data["Projects"],
        data["Communication_Score"]
    ]], columns=[
        "GPA",
        "Coding_Score",
        "Internship",
        "Projects",
        "Communication_Score"
    ])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return jsonify({
        "prediction": int(prediction),
        "placement_probability": round(float(probability), 4)
    })

if __name__ == "__main__":
    app.run(debug=True)
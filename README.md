# Placement Probability Predictor

## 📌 Project Overview
This project predicts the probability of student placement based on academic and skill-related features using Logistic Regression.

## 🎯 Objective
To build a simple machine learning pipeline that:
- Generates synthetic student data
- Trains a classification model
- Predicts placement probability

## 📊 Features Used
- GPA (0–10)
- Coding Score (0–100)
- Internship Experience (0 or 1)
- Number of Projects
- Communication Score (0–10)

Target Variable:
- Placed (0 = Not Placed, 1 = Placed)

## 🤖 Model Used
Logistic Regression

## 📁 Project Structure

placement_predictor/
│
├── data/
├── model/
├── main.py
├── train_model.py
├── predict.py
└── README.md

## ▶️ How to Run

Step 1: Generate Dataset
python main.py

Step 2: Train Model
python train_model.py

Step 3: Predict
python predict.py

## ✅ Output
The system predicts whether a student has HIGH or LOW probability of placement.

---
Developed as part of internship assignment.
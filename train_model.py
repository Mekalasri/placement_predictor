import pandas as pd
import os
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("data/student_data.csv")

X = df.drop("Placed", axis=1)
y = df["Placed"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("✅ Model trained successfully!")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Save model
if not os.path.exists("model"):
    os.makedirs("model")

joblib.dump(model, "model/placement_model.pkl")
print("\n✅ Model saved inside model folder!")

# ----------------- VISUALIZATION -----------------

cm = confusion_matrix(y_test, y_pred)

plt.figure()
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

if not os.path.exists("visualizations"):
    os.makedirs("visualizations")

plt.savefig("visualizations/confusion_matrix.png")
print("📊 Confusion matrix saved in visualizations folder!")
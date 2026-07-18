import os
import re
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# -----------------------------
# Create folders
# -----------------------------
os.makedirs("models", exist_ok=True)
os.makedirs("results", exist_ok=True)

# -----------------------------
# Load Dataset
# -----------------------------
print("Loading dataset...")

df = pd.read_csv("dataset/resume/Resume/Resume.csv")

df = df[['Resume_str', 'Category']].dropna()

print("Dataset Shape:", df.shape)

# -----------------------------
# Text Cleaning
# -----------------------------
def clean_text(text):
    text = text.lower()

    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"www\S+", " ", text)
    text = re.sub(r"\S+@\S+", " ", text)

    text = re.sub(r"[^a-zA-Z ]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()

print("Cleaning resumes...")

df["Resume_str"] = df["Resume_str"].apply(clean_text)

# -----------------------------
# Features & Labels
# -----------------------------
X = df["Resume_str"]
y = df["Category"]

# -----------------------------
# Train/Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# -----------------------------
# Model Pipeline
# -----------------------------
model = Pipeline([

    ("tfidf",
     TfidfVectorizer(
         stop_words="english",
         max_features=15000,
         ngram_range=(1,2),
         min_df=2,
         max_df=0.95,
         sublinear_tf=True
     )
    ),

    ("classifier",
     LinearSVC(class_weight="balanced"))
])

print("\nTraining model...\n")

model.fit(X_train, y_train)

# -----------------------------
# Prediction
# -----------------------------
pred = model.predict(X_test)

# -----------------------------
# Accuracy
# -----------------------------
accuracy = accuracy_score(y_test, pred)

print("="*60)
print(f"Accuracy : {accuracy*100:.2f}%")
print("="*60)

# -----------------------------
# Classification Report
# -----------------------------
report = classification_report(
    y_test,
    pred,
    zero_division=0
)

print(report)

with open("results/classification_report.txt","w") as f:
    f.write(report)

# -----------------------------
# Confusion Matrix
# -----------------------------
cm = confusion_matrix(y_test, pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=model.classes_
)

fig, ax = plt.subplots(figsize=(16,16))

disp.plot(
    cmap="Blues",
    xticks_rotation=90,
    ax=ax,
    colorbar=False
)

plt.title("Confusion Matrix")
plt.tight_layout()

plt.savefig("results/confusion_matrix.png", dpi=300)

plt.close()

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model, "models/resume_classifier.pkl")

print("\nModel Saved Successfully!")

print("\nFiles Generated:")
print("✔ models/resume_classifier.pkl")
print("✔ results/classification_report.txt")
print("✔ results/confusion_matrix.png")
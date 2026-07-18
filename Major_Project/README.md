# AI Resume Analyzer & ATS Score Predictor

## Overview

AI Resume Analyzer & ATS Score Predictor is a Flask-based web application that analyzes resumes using Artificial Intelligence and Natural Language Processing (NLP). The system evaluates resumes by extracting candidate information, predicting the most suitable job category using a trained machine learning model, calculating an ATS (Applicant Tracking System) score, identifying missing skills, recommending relevant job roles, and generating downloadable reports.

This project was enhanced with a resume dataset (50MB+) and a trained machine learning model to improve resume classification accuracy.

---

## Features

- Upload Resume (PDF)
- Resume Text Extraction
- Name, Email & Phone Number Extraction
- AI-Based Resume Category Prediction
- ATS Score Calculation
- Skill Extraction
- Missing Skill Identification
- Job Role Recommendations
- PDF Report Generation
- REST API Support
- User-Friendly Flask Web Interface

---

## Machine Learning Model

### Dataset

- Resume Dataset (50MB+)
- 2,484 resumes
- 24 job categories

### Model

- TF-IDF Vectorization
- Linear Support Vector Classifier (LinearSVC)
- Text Cleaning & Preprocessing
- Balanced Class Weights

### Model Performance

- Accuracy: **72.23%**

---

## Project Structure

```
AI Resume Analyzer/
│
├── app.py
├── ats.py
├── recommender.py
├── resume_parser.py
├── report_generator.py
│
├── dataset/
│   └── Resume.csv
│
├── models/
│   └── resume_classifier.pkl
│
├── results/
│   ├── classification_report.txt
│   └── confusion_matrix.png
│
├── templates/
├── static/
├── uploads/
│
├── prepare_dataset.py
├── train_model.py
├── predict.py
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- PDFPlumber / PyPDF2
- HTML
- CSS
- JavaScript

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer.git
```

Navigate to the project

```bash
cd AI-Resume-Analyzer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open in browser

```
http://127.0.0.1:5000
```

---

## Training the Model

Prepare the dataset

```bash
python prepare_dataset.py
```

Train the model

```bash
python train_model.py
```

Test prediction

```bash
python predict.py
```

---

## Workflow

1. Upload Resume (PDF)
2. Extract Resume Text
3. Predict Resume Category using AI Model
4. Extract Candidate Details
5. Calculate ATS Score
6. Identify Missing Skills
7. Recommend Suitable Job Roles
8. Generate Downloadable Report

---

## Future Enhancements

- Deep Learning-based Resume Classification
- Resume Ranking System
- Resume vs Job Description Matching
- Semantic Similarity using Sentence Transformers
- LLM-powered Resume Feedback
- Multi-language Resume Support
- Resume Improvement Suggestions

---

## Results

- Successfully trained on a 50MB+ resume dataset.
- AI-powered resume category prediction.
- ATS score calculation with skill gap analysis.
- Automatic report generation.
- Improved project functionality using Machine Learning.

---

## Author

**Sanket Kolhe**

Computer Engineering Student

MIT Academy of Engineering, Pune

GitHub: https://github.com/SanketKolhe2005

LinkedIn: https://www.linkedin.com/in/sanket-kolhe-b2683525b

---

## License

This project is developed for educational and internship purposes.

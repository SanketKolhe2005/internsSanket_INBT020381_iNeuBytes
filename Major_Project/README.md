# 🤖 AI Resume Analyzer & ATS Score Predictor

An AI-powered Resume Analyzer built using **Flask**, **Python**, and **NLP** that analyzes uploaded resumes, extracts important information, calculates an ATS (Applicant Tracking System) score, identifies missing skills, recommends suitable job roles, and generates a downloadable PDF report.

---

## 📌 Features

- 📄 Upload Resume (PDF)
- 👤 Extract Candidate Name
- 📧 Extract Email Address
- 📱 Extract Phone Number
- 🧠 AI-Based Skill Extraction
- 📊 ATS Score Calculation
- ❌ Missing Skills Detection
- 💼 Job Role Recommendation
- 💡 Resume Improvement Suggestions
- 📄 Download PDF Analysis Report
- 🌐 REST API for Resume Analysis
- 🎨 Modern Responsive User Interface

---

## 🛠️ Technologies Used

### Backend
- Python
- Flask
- ReportLab

### AI / NLP
- PyMuPDF (fitz)
- Pandas
- Scikit-learn

### Frontend
- HTML5
- CSS3
- JavaScript

### Deployment
- Render
- Gunicorn

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── ats.py
├── recommender.py
├── resume_parser.py
├── report_generator.py
├── skills.csv
├── job_roles.csv
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── uploads/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
```

### Move to Project Folder

```bash
cd AI-Resume-Analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🚀 API Endpoint

### Analyze Resume

**POST**

```
/api/analyze
```

### Form Data

| Key | Type |
|------|------|
| resume | File |

### Sample JSON Response

```json
{
  "success": true,
  "name": "John Doe",
  "email": "john@gmail.com",
  "phone": "9876543210",
  "ats_score": 85,
  "skills": [
    "Python",
    "Flask",
    "SQL"
  ],
  "recommended_roles": [
    "AI Engineer",
    "Python Developer"
  ]
}
```

---

## 📊 ATS Score Parameters

The ATS score is calculated based on:

- Technical Skills
- Programming Languages
- AI/ML Libraries
- Frameworks
- Resume Keywords

---

## 💼 Recommended Job Roles

- AI Engineer
- Machine Learning Engineer
- Data Scientist
- Data Analyst
- Python Developer
- Full Stack Developer

---

## 📸 Screenshots

### Home Page

(Add Screenshot Here)

### Resume Analysis Dashboard

(Add Screenshot Here)

### PDF Report

(Add Screenshot Here)

### Postman API Testing

(Add Screenshot Here)

---

## 📈 Future Improvements

- Experience Extraction
- Education Detection
- Certifications Extraction
- Resume Ranking
- AI Chat Assistant
- Multiple Resume Comparison
- Resume Grammar Checker
- Resume Keyword Optimization
- OCR Support for Image Resumes

---

## 👨‍💻 Author

**Sanket Kolhe**

- GitHub: https://github.com/SanketKolhe2005
- LinkedIn: https://www.linkedin.com/in/sanket-kolhe-b2683525b

---

## 📄 License

This project is developed for educational and internship purposes.

---

## ⭐ If you found this project helpful, don't forget to star the repository!
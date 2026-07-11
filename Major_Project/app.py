from flask import Flask, render_template, request, send_file, jsonify, session
import os
from werkzeug.utils import secure_filename

from resume_parser import extract_text, extract_name, extract_email, extract_phone
from ats import extract_skills, calculate_ats, missing_skills
from recommender import recommend_jobs
from report_generator import generate_report

app = Flask(__name__)
app.secret_key = "resume_analyzer_secret_key"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:
        return "No file uploaded."

    file = request.files["resume"]

    if file.filename == "":
        return "Please choose a PDF file."

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    # -------------------------
    # Extract Resume Text
    # -------------------------

    text = extract_text(filepath)

    # Personal Details

    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)

    # Skills

    skills = extract_skills(text)

    score = calculate_ats(skills)

    missing = missing_skills(skills)

    jobs = recommend_jobs(skills)

    # -------------------------
    # Grade
    # -------------------------

    if score >= 80:
        grade = "Excellent ⭐"

    elif score >= 60:
        grade = "Good 👍"

    elif score >= 40:
        grade = "Average 🙂"

    else:
        grade = "Needs Improvement ⚠️"

    # -------------------------
    # Suggestions
    # -------------------------

    suggestions = []

    if len(missing) == 0:

        suggestions.append(
            "Excellent resume! No major missing skills detected."
        )

    else:

        for skill in missing[:5]:

            suggestions.append(
                f"Consider adding or learning {skill} if you have experience."
            )

    # -------------------------
    # Save Data for PDF Report
    # -------------------------

    session["name"] = name
    session["email"] = email
    session["phone"] = phone
    session["score"] = score
    session["skills"] = skills
    session["jobs"] = jobs

    # -------------------------
    # Render Result Page
    # -------------------------

    return render_template(

        "result.html",

        filename=filename,

        name=name,

        email=email,

        phone=phone,

        score=score,

        grade=grade,

        skills=skills,

        missing=missing,

        jobs=jobs,

        suggestions=suggestions,

        resume_text=text

    )
    
    # -------------------------
# Download PDF Report
# -------------------------

@app.route("/download")
def download():

    if "name" not in session:
        return "Please analyze a resume first."

    generate_report(

        "resume_report.pdf",

        session.get("name"),

        session.get("email"),

        session.get("phone"),

        session.get("score"),

        session.get("skills"),

        session.get("jobs")

    )

    return send_file(

        "resume_report.pdf",

        as_attachment=True,

        download_name="AI_Resume_Analyzer_Report.pdf"

    )


# -------------------------
# REST API
# -------------------------

@app.route("/api/analyze", methods=["POST"])
def api_analyze():

    if "resume" not in request.files:

        return jsonify({

            "success": False,

            "message": "No resume uploaded"

        }), 400

    file = request.files["resume"]

    if file.filename == "":

        return jsonify({

            "success": False,

            "message": "No file selected"

        }), 400

    filename = secure_filename(file.filename)

    filepath = os.path.join(

        app.config["UPLOAD_FOLDER"],

        filename

    )

    file.save(filepath)

    text = extract_text(filepath)

    name = extract_name(text)

    email = extract_email(text)

    phone = extract_phone(text)

    skills = extract_skills(text)

    score = calculate_ats(skills)

    missing = missing_skills(skills)

    jobs = recommend_jobs(skills)

    return jsonify({

        "success": True,

        "name": name,

        "email": email,

        "phone": phone,

        "ats_score": score,

        "skills": skills,

        "missing_skills": missing,

        "recommended_roles": jobs

    })


# -------------------------
# Run Flask
# -------------------------

if __name__ == "__main__":

    app.run(debug=True)
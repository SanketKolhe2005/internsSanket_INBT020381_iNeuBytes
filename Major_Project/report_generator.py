from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

def generate_report(filename, name, email, phone, score, skills, jobs):

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Resume Analyzer Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Name:</b> {name}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Email:</b> {email}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Phone:</b> {phone}", styles["BodyText"]))

    story.append(Paragraph(f"<b>ATS Score:</b> {score}%", styles["BodyText"]))

    story.append(Paragraph("<b>Skills</b>", styles["Heading2"]))

    story.append(Paragraph(", ".join(skills), styles["BodyText"]))

    story.append(Paragraph("<b>Recommended Roles</b>", styles["Heading2"]))

    story.append(Paragraph(", ".join(jobs), styles["BodyText"]))

    pdf.build(story)
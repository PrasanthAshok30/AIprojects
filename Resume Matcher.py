import streamlit as st
import PyPDF2
import docx2txt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import io

st.set_page_config(page_title="Resume Matcher AI", layout="centered")
st.title("🤖 Resume Matcher AI")
st.write("Upload your resume and paste a job description to see how well they match.")

# Function to extract text from uploaded resume
def extract_text(file):
    if file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    else:
        return ""

# Upload resume
resume_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

# Paste job description
job_description = st.text_area("Paste the job description here")

# Match button
if st.button("🔍 Match Now"):
    if resume_file is not None and job_description.strip():
        resume_text = extract_text(resume_file)

        # Vectorize and compute similarity
        vectorizer = TfidfVectorizer().fit_transform([resume_text, job_description])
        similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]

        score = round(similarity * 100, 2)
        st.success(f"✅ Match Score: {score}%")

        if score > 75:
            st.info("🎯 Great match! You’re a strong fit for this role.")
        elif score > 50:
            st.warning("⚠️ Decent match. Tailor your resume for a better fit.")
        else:
            st.error("❌ Low match. Consider rewriting your resume or applying to a better-fitting job.")
    else:
        st.error("Please upload your resume and paste a job description.")

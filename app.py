import os
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
from pdf2image import convert_from_path
import pytesseract
import pdfplumber

# Load evironment variables
load_dotenv()

# Configure Google Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text =""
    try:
        # Try direct text extraction 
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
        if text.strip():
            return text.strip()
    except Exception as e:
        print(f"Direct text extraction fail : {e} ")
    # fall back to OCR  for image-based PDFs
    print ("Failing back to OCR for image-based PDF")
    try:
        images = convert_from_path(pdf_path)
        for image in images:
            page_text = pytesseract.image_to_strict(image)
            text += page_text + "\n"
    except Exception as e:
        print(f'OCR failed: {e}')
    return text.strip()
    
# function to analyze resume using Google Gemini AI
def analyze_resume(resume_text, job_desciption=None):
    if not resume_text:
        return {"error": "Resume text is required for analysis"}
    model = genai.GenerativeModel("gemini-1.5-flash")

    base_prompt = f"""
    You are an experienced HR headhunter with technical experience in the field of the following job roles: 
    Data Sciencist, Data Analyst, Machine Learning Engineer, Data Engineer, Bussiness Analyst, your task is 
    to review the provided resume. Please share proffessional feedback on whether the candidate profile matches
    with the role. In addition, mention the skills the candidate alreayd have and mention some skills that need
    improvement, also suggest some courses/projects the candidate can do to improve their profile.

    Resume:
    {resume_text}
"""
    if job_desciption:
        base_prompt += f"""
        In addition, compare this resume to the following description:
        Job Description:
        {job_desciption}
        """
    response = model.generate_content(base_prompt)

    analysis = response.text.strip()
    return analysis 
# Streamlit app
st.set_page_config(page_title="Resume Analyzer", layout="wide")

# Title
st.title("AI Resume Analyzer")
st.write("Analyze your resume and match it with job descriptions using Google Gemini AI.")

col1, col2 = st.columns(2)

with col1:
    uploaded_file= st.file_uploader("Upload your Resume (PDF)", type = "pdf")
with col2:
    job_description = st.text_area("Paste Job Description: ",placeholder="Paste the job description here")

if uploaded_file is not None:
    st.sucess("Resume uploaded successfully!")
else:
    st.warning("Please upload a resume in pdf format to proceed.")

st.markdown("<div style= 'padding-top : 10px ; '></div>", unsafe_allow_html=True)
if uploaded_file:
# save file locally for processing
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
# extract text from pdf
    resume_text = extract_text_from_pdf("uploaded_resume.pdf")
    
    if st.button("Analyze Resume"):
        with st.spinner("Analyzing Resume..."):
            try: 
                # analyze resume
                analysis = analyze_resume(resume_text, job_description)
                st.success("Analysis Complete!")
                st.write(analysis)
            except Exception as e:
                st.error(f"Analysis failed: {e}")

# footer
st.markdown("---")
st.markdown(""" <p stlyle='text-align: center;' >Powered by <b>Streamlit</b> and <b>Google Gemini AI</b> | Developed by <a href='https://www.linkedin.com/in/ky-kate-nguyen' target='_blank' style='text-decoration: none; color:#FFFFFF'
            <b>Kate Nguyen</b></a></p>""", unsafe_allow_html=True)
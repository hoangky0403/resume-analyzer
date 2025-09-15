📄 AI Resume Analyzer

Analyze your resume and match it with job descriptions using Google Gemini AI.
This app extracts text from PDF resumes (both text-based and scanned) and provides tailored feedback on skills, improvements, and career recommendations.

✨ Features

Upload resume in PDF format (supports both text-based & scanned PDFs)

Automatic text extraction with pdfplumber and OCR fallback for image-based PDFs

AI-powered resume analysis using Google Gemini

Optional comparison with a job description

Feedback includes:

Key strengths

Skills to improve

Suggested courses or projects

⚙️ Setup

Clone the repository

Install dependencies listed in requirements.txt

Create a .env file in the project root and add your Gemini API key:

GOOGLE_API_KEY=your_api_key_here

Run the app with Streamlit

▶️ Usage

Open the app in your browser

Upload your resume in PDF format

Optionally paste a job description

Click Analyze Resume to generate AI-powered feedback

🚀 Deployment on Hugging Face Spaces

Push the repository to Hugging Face Spaces

Add your GOOGLE_API_KEY in Settings → Secrets

Hugging Face will automatically build and launch the app

📦 Requirements

Streamlit

python-dotenv

Pillow

google-generativeai

pdf2image

pytesseract

pdfplumber

👩‍💻 Author

Developed by Ky Nguyen
Powered by Streamlit and Google Gemini AI

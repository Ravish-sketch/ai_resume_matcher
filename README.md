<h1 align="center">🚀 AI Resume Screening & Job Matching System</h1>

<p align="center">
  <a href="https://ai-resume-matcher-gemini.streamlit.app/" target="_blank">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open in Streamlit">
  </a>
  <a href="https://github.com/Ravish-sketch/ai_resume_matcher">
    <img src="https://img.shields.io/github/stars/Ravish-sketch/ai_resume_matcher?style=social" alt="GitHub Stars">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
  </a>
  <img src="https://img.shields.io/badge/AI-Gemini%202.5%20Flash-orange" alt="Gemini AI">
</p>

<p align="center">
  <strong>An intelligent web application that matches your resume against job descriptions using advanced NLP and Google's Gemini AI.</strong>
</p>

---

## 🌟 Overview

The **AI Resume Matcher** is a powerful Streamlit-based web application designed to help job seekers and recruiters instantly evaluate the alignment between a candidate's resume and a specific job description. 

Instead of simple keyword matching, this tool utilizes **Sentence Transformers** for semantic similarity and **Google's Gemini 2.5 Flash** for deep contextual analysis, providing actionable insights to improve resume formatting and ATS (Applicant Tracking System) scores.

---

## ✨ Key Features

- 📄 **Seamless Uploads**: Upload resumes in PDF or DOCX format.
- 📋 **Flexible JD Inputs**: Directly paste job descriptions or upload them as files.
- 🧠 **Deep AI Analysis**: Leverages Google's Gemini API to intelligently extract skills and analyze gaps.
- 📊 **Dynamic Dashboard**: Beautiful UI featuring interactive charts (powered by Plotly) to visualize skill match percentages.
- 🎯 **Actionable Feedback**: Receive concrete "Resume Tweaks" and "ATS Formatting Feedback" customized to your specific resume and target job.

---

## 🛠️ How It Was Built (Tech Stack)

The architecture is built on a modern Python AI stack:

- **Frontend**: [Streamlit](https://streamlit.io/) (with custom Glassmorphism CSS for a premium UI)
- **AI & LLM**: [Google Generative AI (Gemini 2.5 Flash)](https://aistudio.google.com/) for intelligent skill extraction and contextual feedback.
- **NLP / Embeddings**: `sentence-transformers` (`all-MiniLM-L6-v2`) and `scikit-learn` for computing cosine similarity between texts.
- **PDF Processing**: `PyMuPDF` (fitz) and `pdfplumber` for robust text extraction.
- **Data Visualization**: `Plotly` and `Pandas` for rendering the Skill Gap Analysis charts.

### ⚙️ How It Works (The Workflow)
1. **Extraction**: The system parses raw text from the uploaded PDF resume and Job Description.
2. **Embedding**: The texts are converted into dense vector embeddings to calculate a baseline "Semantic Similarity" score.
3. **AI Processing**: The Gemini model analyzes both texts to extract explicit skills and determine what the candidate lacks.
4. **Scoring**: A composite match score is calculated by combining semantic alignment and skill coverage.
5. **Reporting**: Results are rendered on a responsive, dark-mode dashboard.

---

## 🚀 Step-by-Step Installation & Usage Guide

Follow these steps to run the project locally on your machine:

### Prerequisites
- Python 3.8 or higher installed on your system.
- A free API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 1. Clone the Repository
```bash
git clone https://github.com/Ravish-sketch/ai_resume_matcher.git
cd ai_resume_matcher
```

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
1. In the root directory of the project, create a new file named `.env`.
2. Add your Gemini API key to the file like this:
```env
GEMINI_API_KEY="your_actual_gemini_api_key_here"
```

### 5. Run the Application
```bash
streamlit run app.py
```
*The app will automatically open in your default web browser at `http://localhost:8501`.*

---

## 📁 Project Structure

```text
ai_resume_matcher/
├── app.py                      # Main Streamlit application entry point
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (API Keys - not in repo)
├── src/
│   ├── ai/                     # AI logic (Embeddings, Gemini LLM Engine, Matcher)
│   ├── config/                 # Project configurations and settings
│   ├── parser/                 # PDF and text extraction logic
│   └── ui/                     # UI components, Sidebar, and Dashboard layouts
└── outputs/                    # Local storage for logs and generated reports
```

---

<p align="center">Made with ❤️ using Python and Streamlit.</p>

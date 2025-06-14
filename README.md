# AI Resume Screening System

## 🔍 Overview
Upload a resume (PDF/DOCX/IMG) and get a similarity score against a job description using BERT embeddings and cosine similarity.

## 🛠️ Features
- Resume parsing (PDF, DOCX, Image)
- BERT-based semantic ranking
- FastAPI backend for uploads
- OCR support

## 🚀 Running Locally

```bash
# Step 1: Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the server
uvicorn app.main:app --reload

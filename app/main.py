from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.resume_parser import extract_resume_text
from app.model import calculate_similarity
from app.utils import save_uploaded_file, load_job_description

app = FastAPI(title="AI Resume Screening System")

@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    try:
        file_path = save_uploaded_file(file)
        resume_text = extract_resume_text(file_path)
        jd_text = load_job_description()
        similarity_score = calculate_similarity(resume_text, jd_text)
        return JSONResponse({"similarity_score": round(similarity_score * 100, 2)})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=400)

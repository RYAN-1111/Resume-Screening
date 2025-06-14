from pdfminer.high_level import extract_text
import docx2txt
import pytesseract
import cv2
import os

def extract_text_from_pdf(file_path):
    return extract_text(file_path)

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

def extract_text_from_image(file_path):
    image = cv2.imread(file_path)
    return pytesseract.image_to_string(image)

def extract_resume_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    elif file_path.lower().endswith((".png", ".jpg", ".jpeg")):
        return extract_text_from_image(file_path)
    else:
        raise ValueError("Unsupported file format.")
    
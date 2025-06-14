import shutil
import tempfile

def save_uploaded_file(uploaded_file):
    suffix = "." + uploaded_file.filename.split('.')[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        shutil.copyfileobj(uploaded_file.file, tmp)
        return tmp.name

def load_job_description():
    with open("job_description.txt", "r") as f:
        return f.read()

from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
import pdfplumber
import io
from ..dependencies import get_supabase

router = APIRouter(prefix="/files", tags=["files"])

@router.post("/upload")
async def upload_files(files: List[UploadFile] = File(...), supabase=Depends(get_supabase)):
    results = []
    for file in files:
        if file.filename.endswith('.pdf'):
            try:
                # Read PDF content
                content = await file.read()
                text = extract_pdf_text(content)
                
                # Upload to Supabase Storage
                file_path = f"notes/{file.filename}"
                supabase.storage.from_("notes").upload(file_path, content)
                
                # Store metadata in database
                file_data = {
                    "filename": file.filename,
                    "content": text,
                    "path": file_path
                }
                results.append(file_data)
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))
        else:
            raise HTTPException(status_code=400, detail="Only PDF files are supported")
    
    return {"uploaded_files": results}

def extract_pdf_text(content: bytes) -> str:
    with pdfplumber.open(io.BytesIO(content)) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages) 
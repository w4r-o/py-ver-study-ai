from fastapi import APIRouter, Depends, UploadFile, File
from ..services.database import DatabaseService
from ..services.pdf_service import extract_text_from_pdf 
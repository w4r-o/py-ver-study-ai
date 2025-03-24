from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .routers import auth, files, tests
from .config import settings

app = FastAPI(
    title="StudyAI API",
    description="AI-powered study assistant that generates practice tests from notes",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(files.router, prefix="/api/files", tags=["Files"])
app.include_router(tests.router, prefix="/api/tests", tags=["Tests"])

@app.get("/")
async def root():
    return {"message": "Welcome to StudyAI API"} 
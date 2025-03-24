from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from ..dependencies import get_supabase, get_ai_client

router = APIRouter(prefix="/tests", tags=["tests"])

class TestRequest(BaseModel):
    content: str
    grade_level: int
    subject: Optional[str]
    num_questions: int = 10

@router.post("/generate")
async def generate_test(
    request: TestRequest,
    ai_client=Depends(get_ai_client),
    supabase=Depends(get_supabase)
):
    try:
        # Generate test using AI
        prompt = create_test_prompt(request)
        response = ai_client.generate_test(prompt)
        
        # Store test in database
        test_data = {
            "questions": response["questions"],
            "grade_level": request.grade_level,
            "subject": response["subject"]
        }
        
        result = supabase.table("tests").insert(test_data).execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def create_test_prompt(request: TestRequest) -> str:
    return f"""
    Generate a test based on the following parameters:
    Grade Level: {request.grade_level}
    Subject: {request.subject or 'Determine from content'}
    Number of Questions: {request.num_questions}
    
    Content:
    {request.content}
    
    Generate questions in the following format:
    1. Multiple Choice Questions
    2. Knowledge Questions
    3. Thinking Questions
    4. Application Questions
    5. Communication Questions
    """ 
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from ..dependencies import get_supabase

router = APIRouter(prefix="/auth", tags=["auth"])

class UserCreate(BaseModel):
    email: str
    password: str
    grade_level: Optional[int]

@router.post("/signup")
async def signup(user: UserCreate, supabase=Depends(get_supabase)):
    try:
        response = supabase.auth.sign_up({
            "email": user.email,
            "password": user.password,
            "options": {
                "data": {
                    "grade_level": user.grade_level
                }
            }
        })
        return response.dict()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login(user: UserCreate, supabase=Depends(get_supabase)):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": user.email,
            "password": user.password
        })
        return response.dict()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 
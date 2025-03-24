from pydantic import BaseModel, UUID4
from typing import Optional, Dict, List
from datetime import datetime

class UserProfile(BaseModel):
    id: UUID4
    grade_level: Optional[int]
    created_at: datetime
    updated_at: datetime

class StudyMaterial(BaseModel):
    id: UUID4
    user_id: UUID4
    title: str
    content: Optional[str]
    file_path: Optional[str]
    subject: Optional[str]
    grade_level: Optional[int]
    created_at: datetime

class Test(BaseModel):
    id: UUID4
    user_id: UUID4
    material_id: UUID4
    title: str
    subject: Optional[str]
    grade_level: Optional[int]
    questions: List[Dict]
    created_at: datetime

class TestResult(BaseModel):
    id: UUID4
    user_id: UUID4
    test_id: UUID4
    score: float
    answers: Dict
    feedback: Optional[str]
    completed_at: datetime 
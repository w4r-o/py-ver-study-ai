from pydantic import BaseModel
from typing import List, Optional

class Question(BaseModel):
    text: str
    options: List[str]
    correct_answer: str
    type: str
    explanation: Optional[str] = None

class Test(BaseModel):
    title: str
    subject: str
    grade_level: int
    questions: List[Question]
    created_by: str 
from fastapi import APIRouter, Depends
from ..services.database import DatabaseService
from ..services.ai_service import generate_test
from ..dependencies import get_current_user

router = APIRouter()
db = DatabaseService()

@router.post("/generate/{material_id}")
async def create_test(
    material_id: str,
    current_user = Depends(get_current_user)
):
    # Get study material
    material = await db.get_study_material(material_id)
    
    # Generate test using AI
    test_content = await generate_test(
        content=material.content,
        grade_level=material.grade_level,
        subject=material.subject
    )
    
    # Save test to database
    test = await db.create_test(
        user_id=current_user.id,
        material_id=material_id,
        title=f"Test for {material.title}",
        questions=test_content["questions"],
        subject=material.subject,
        grade_level=material.grade_level
    )
    
    return test 
from typing import Dict, List
import httpx
from ..config import settings

async def generate_test(content: str, grade_level: int, subject: str) -> Dict:
    prompt = f"""
    Generate a 
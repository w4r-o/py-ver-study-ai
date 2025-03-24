from typing import Optional, List, Dict
from ..dependencies import get_supabase
from ..models.database import UserProfile, StudyMaterial, Test, TestResult

class DatabaseService:
    def __init__(self):
        self.supabase = get_supabase()

    async def create_user_profile(self, user_id: str, grade_level: Optional[int] = None) -> UserProfile:
        data = {
            'id': user_id,
            'grade_level': grade_level
        }
        result = self.supabase.table('user_profiles').insert(data).execute()
        return UserProfile(**result.data[0])

    async def create_study_material(self, 
                                  user_id: str, 
                                  title: str, 
                                  content: Optional[str] = None,
                                  file_path: Optional[str] = None,
                                  subject: Optional[str] = None,
                                  grade_level: Optional[int] = None) -> StudyMaterial:
        data = {
            'user_id': user_id,
            'title': title,
            'content': content,
            'file_path': file_path,
            'subject': subject,
            'grade_level': grade_level
        }
        result = self.supabase.table('study_materials').insert(data).execute()
        return StudyMaterial(**result.data[0])

    async def create_test(self,
                         user_id: str,
                         material_id: str,
                         title: str,
                         questions: List[Dict],
                         subject: Optional[str] = None,
                         grade_level: Optional[int] = None) -> Test:
        data = {
            'user_id': user_id,
            'material_id': material_id,
            'title': title,
            'questions': questions,
            'subject': subject,
            'grade_level': grade_level
        }
        result = self.supabase.table('tests').insert(data).execute()
        return Test(**result.data[0])

    async def save_test_result(self,
                             user_id: str,
                             test_id: str,
                             score: float,
                             answers: Dict,
                             feedback: Optional[str] = None) -> TestResult:
        data = {
            'user_id': user_id,
            'test_id': test_id,
            'score': score,
            'answers': answers,
            'feedback': feedback
        }
        result = self.supabase.table('test_results').insert(data).execute()
        return TestResult(**result.data[0])

    async def get_user_materials(self, user_id: str) -> List[StudyMaterial]:
        result = self.supabase.table('study_materials')\
            .select('*')\
            .eq('user_id', user_id)\
            .execute()
        return [StudyMaterial(**item) for item in result.data]

    async def get_user_tests(self, user_id: str) -> List[Test]:
        result = self.supabase.table('tests')\
            .select('*')\
            .eq('user_id', user_id)\
            .execute()
        return [Test(**item) for item in result.data] 
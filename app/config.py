from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "StudyAI"
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # External Services
    DEEPSEEK_API_KEY: str
    SUPABASE_URL: str
    SUPABASE_KEY: str
    
    # Database
    DATABASE_URL: str = "sqlite:///./test.db"  # Default SQLite for development
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings() 
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from supabase import create_client, Client
from .config import settings
import httpx

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_supabase() -> Client:
    return create_client(
        supabase_url=settings.SUPABASE_URL,
        supabase_key=settings.SUPABASE_KEY
    )

# Helper function to get database connection
async def get_db():
    supabase = get_supabase()
    try:
        yield supabase
    finally:
        # Supabase client doesn't need explicit closure
        pass

async def get_ai_client():
    async with httpx.AsyncClient() as client:
        client.headers.update({"Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}"})
        return client

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        supabase = get_supabase()
        user = supabase.auth.get_user(token)
        if user is None:
            raise credentials_exception
        return user
    except Exception:
        raise credentials_exception 
"""
Supabase Auth integration outline for FastAPI app.
- Supports email/password and Google OAuth.
- Use supabase-py client for authentication.
"""

import os

from fastapi import APIRouter, HTTPException, status
from supabase import Client, create_client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

auth_router = APIRouter()


@auth_router.post("/auth/login")
def login(email: str, password: str):
    result = supabase.auth.sign_in_with_password({"email": email, "password": password})
    if not result.user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    return {"access_token": result.session.access_token}


@auth_router.post("/auth/signup")
def signup(email: str, password: str):
    result = supabase.auth.sign_up({"email": email, "password": password})
    if not result.user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Signup failed"
        )
    return {"message": "Signup successful. Please check your email to confirm."}

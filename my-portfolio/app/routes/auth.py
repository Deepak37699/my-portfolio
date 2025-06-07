from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.services.auth_service import authenticate_user, create_access_token
from app.models.user import User
from app.utils.security import verify_password

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(login_request: LoginRequest):
    user = authenticate_user(login_request.username, login_request.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/logout")
async def logout():
    return {"message": "Successfully logged out"}
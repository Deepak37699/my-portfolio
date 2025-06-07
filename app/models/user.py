from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username")
    email: Optional[EmailStr] = Field(None, description="User email")
    hashed_password: str = Field(..., description="Hashed password")
    is_active: bool = Field(default=True, description="Whether user is active")
    created_date: datetime = Field(default_factory=datetime.now, description="User creation date")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, description="Plain password")


class UserLogin(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=1)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Skill(BaseModel):
    id: str = Field(..., description="Unique identifier for the skill")
    name: str = Field(..., min_length=1, max_length=100, description="Skill name")
    category: str = Field(..., min_length=1, max_length=100, description="Skill category")
    proficiency: int = Field(..., ge=0, le=100, description="Proficiency level (0-100)")
    years_experience: int = Field(..., ge=0, description="Years of experience")
    icon: Optional[str] = Field(None, description="Icon filename or CSS class")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class SkillCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    category: str = Field(..., min_length=1, max_length=100)
    proficiency: int = Field(..., ge=0, le=100)
    years_experience: int = Field(..., ge=0)
    icon: Optional[str] = None


class SkillUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    category: Optional[str] = Field(None, min_length=1, max_length=100)
    proficiency: Optional[int] = Field(None, ge=0, le=100)
    years_experience: Optional[int] = Field(None, ge=0)
    icon: Optional[str] = None

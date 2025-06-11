from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Education(BaseModel):
    id: str = Field(..., description="Unique identifier for the education entry")
    degree: str = Field(..., min_length=1, max_length=200, description="Degree or qualification")
    institution: str = Field(..., min_length=1, max_length=200, description="Educational institution")
    year: str = Field(..., description="Year of completion or expected completion")
    grade: Optional[str] = Field(None, description="Grade, GPA, or percentage")
    field_of_study: Optional[str] = Field(None, description="Field of study or major")
    description: Optional[str] = Field(None, description="Additional description")
    created_date: datetime = Field(default_factory=datetime.now, description="Entry creation date")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class EducationCreate(BaseModel):
    degree: str = Field(..., min_length=1, max_length=200)
    institution: str = Field(..., min_length=1, max_length=200)
    year: str = Field(...)
    grade: Optional[str] = None
    field_of_study: Optional[str] = None
    description: Optional[str] = None


class EducationUpdate(BaseModel):
    degree: Optional[str] = Field(None, min_length=1, max_length=200)
    institution: Optional[str] = Field(None, min_length=1, max_length=200)
    year: Optional[str] = None
    grade: Optional[str] = None
    field_of_study: Optional[str] = None
    description: Optional[str] = None

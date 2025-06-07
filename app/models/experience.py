from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Experience(BaseModel):
    id: str = Field(..., description="Unique identifier for the experience entry")
    job_title: str = Field(..., min_length=1, max_length=200, description="Job title or position")
    company: str = Field(..., min_length=1, max_length=200, description="Company or organization")
    location: Optional[str] = Field(None, description="Job location")
    start_date: str = Field(..., description="Start date (YYYY-MM or YYYY)")
    end_date: Optional[str] = Field(None, description="End date (YYYY-MM or YYYY), null for current")
    is_current: bool = Field(default=False, description="Whether this is the current position")
    description: Optional[str] = Field(None, description="Job description and responsibilities")
    technologies: Optional[list[str]] = Field(default=[], description="Technologies used")
    achievements: Optional[list[str]] = Field(default=[], description="Key achievements")
    created_date: datetime = Field(default_factory=datetime.now, description="Entry creation date")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class ExperienceCreate(BaseModel):
    job_title: str = Field(..., min_length=1, max_length=200)
    company: str = Field(..., min_length=1, max_length=200)
    location: Optional[str] = None
    start_date: str = Field(...)
    end_date: Optional[str] = None
    is_current: bool = False
    description: Optional[str] = None
    technologies: Optional[list[str]] = []
    achievements: Optional[list[str]] = []


class ExperienceUpdate(BaseModel):
    job_title: Optional[str] = Field(None, min_length=1, max_length=200)
    company: Optional[str] = Field(None, min_length=1, max_length=200)
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    is_current: Optional[bool] = None
    description: Optional[str] = None
    technologies: Optional[list[str]] = None
    achievements: Optional[list[str]] = None

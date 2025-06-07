from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from datetime import datetime


class Project(BaseModel):
    id: str = Field(..., description="Unique identifier for the project")
    title: str = Field(..., min_length=1, max_length=200, description="Project title")
    description: str = Field(..., min_length=1, description="Project description")
    technologies: List[str] = Field(..., description="List of technologies used")
    image: Optional[str] = Field(None, description="Project image filename")
    github_url: Optional[HttpUrl] = Field(None, description="GitHub repository URL")
    live_url: Optional[HttpUrl] = Field(None, description="Live demo URL")
    featured: bool = Field(default=False, description="Whether project is featured")
    created_date: datetime = Field(default_factory=datetime.now, description="Project creation date")
    status: str = Field(default="In Progress", description="Project status")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class ProjectCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1)
    technologies: List[str]
    image: Optional[str] = None
    github_url: Optional[HttpUrl] = None
    live_url: Optional[HttpUrl] = None
    featured: bool = False
    status: str = Field(default="In Progress")


class ProjectUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, min_length=1)
    technologies: Optional[List[str]] = None
    image: Optional[str] = None
    github_url: Optional[HttpUrl] = None
    live_url: Optional[HttpUrl] = None
    featured: Optional[bool] = None
    status: Optional[str] = None

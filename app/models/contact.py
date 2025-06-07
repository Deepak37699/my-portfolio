from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime


class ContactMessage(BaseModel):
    id: str = Field(..., description="Unique identifier for the message")
    name: str = Field(..., min_length=1, max_length=100, description="Sender's name")
    email: EmailStr = Field(..., description="Sender's email")
    subject: str = Field(..., min_length=1, max_length=200, description="Message subject")
    message: str = Field(..., min_length=1, description="Message content")
    created_date: datetime = Field(default_factory=datetime.now, description="Message creation date")
    is_read: bool = Field(default=False, description="Whether message has been read")
    status: str = Field(default="unread", description="Message status: unread, read, replied, archived")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class ContactMessageCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    subject: str = Field(..., min_length=1, max_length=200)
    message: str = Field(..., min_length=1)


class ContactMessageUpdate(BaseModel):
    is_read: Optional[bool] = None
    status: Optional[str] = None


class AboutInfo(BaseModel):
    name: str = Field(..., description="Full name")
    title: str = Field(..., description="Professional title")
    bio: str = Field(..., description="Biography/description")
    location: str = Field(..., description="Location")
    email: EmailStr = Field(..., description="Contact email")
    phone: Optional[str] = Field(None, description="Phone number")
    linkedin: Optional[str] = Field(None, description="LinkedIn profile URL")
    github: Optional[str] = Field(None, description="GitHub profile URL")
    twitter: Optional[str] = Field(None, description="Twitter profile URL")
    resume_url: Optional[str] = Field(None, description="Resume/CV URL")
    profile_image: Optional[str] = Field(None, description="Profile image filename")
    years_experience: Optional[int] = Field(None, description="Years of experience")
    education: Optional[List[Dict[str, Any]]] = Field(default=[], description="Education history")
    experience: Optional[List[Dict[str, Any]]] = Field(default=[], description="Work experience")
    certifications: Optional[List[Dict[str, Any]]] = Field(default=[], description="Certifications")
    languages: Optional[List[Dict[str, Any]]] = Field(default=[], description="Languages spoken")
    
    class Config:
        extra = "ignore"  # Ignore extra fields that aren't defined in the model


class AboutInfoUpdate(BaseModel):
    name: Optional[str] = None
    title: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    twitter: Optional[str] = None
    resume_url: Optional[str] = None
    profile_image: Optional[str] = None
    years_experience: Optional[int] = None
    education: Optional[List[Dict[str, Any]]] = None
    certifications: Optional[List[Dict[str, Any]]] = None
    languages: Optional[List[Dict[str, Any]]] = None

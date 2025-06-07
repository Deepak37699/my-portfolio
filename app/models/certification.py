from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Certification(BaseModel):
    id: str = Field(..., description="Unique identifier for the certification")
    name: str = Field(..., min_length=1, max_length=200, description="Certification name")
    issuer: str = Field(..., min_length=1, max_length=200, description="Issuing organization")
    date: str = Field(..., description="Date obtained (YYYY-MM-DD or YYYY-MM)")
    expiry_date: Optional[str] = Field(None, description="Expiry date if applicable")
    credential_id: Optional[str] = Field(None, description="Credential or certificate ID")
    credential_url: Optional[str] = Field(None, description="URL to verify the credential")
    description: Optional[str] = Field(None, description="Additional description")
    skills: Optional[list[str]] = Field(default=[], description="Related skills")
    created_date: datetime = Field(default_factory=datetime.now, description="Entry creation date")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class CertificationCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    issuer: str = Field(..., min_length=1, max_length=200)
    date: str = Field(...)
    expiry_date: Optional[str] = None
    credential_id: Optional[str] = None
    credential_url: Optional[str] = None
    description: Optional[str] = None
    skills: Optional[list[str]] = []


class CertificationUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    issuer: Optional[str] = Field(None, min_length=1, max_length=200)
    date: Optional[str] = None
    expiry_date: Optional[str] = None
    credential_id: Optional[str] = None
    credential_url: Optional[str] = None
    description: Optional[str] = None
    skills: Optional[list[str]] = None

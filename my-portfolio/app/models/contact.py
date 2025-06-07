from pydantic import BaseModel
from datetime import datetime

class ContactMessage(BaseModel):
    id: str
    name: str
    email: str
    message: str
    created_date: datetime
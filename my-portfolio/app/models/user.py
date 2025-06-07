from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    username: str
    hashed_password: str
    is_active: bool
    created_date: datetime = datetime.now()
from pydantic import BaseModel
from typing import List, Optional

class Project(BaseModel):
    id: str
    title: str
    description: str
    technologies: List[str]
    image: str
    github_url: str
    live_url: str
    featured: bool
    created_date: str
from fastapi import APIRouter
from app.models.project import Project
from app.models.skill import Skill
from app.models.contact import Contact
from app.services.json_utils import read_json

router = APIRouter()

@router.get("/about")
async def get_about():
    about_data = read_json("data/about.json")
    return about_data

@router.get("/projects")
async def get_projects():
    projects_data = read_json("data/projects.json")
    return projects_data

@router.get("/skills")
async def get_skills():
    skills_data = read_json("data/skills.json")
    return skills_data

@router.post("/contact")
async def submit_contact(contact: Contact):
    # Logic to handle contact form submission (e.g., save to JSON, send email)
    return {"message": "Contact form submitted successfully!"}
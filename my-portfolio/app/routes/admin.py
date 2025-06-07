from fastapi import APIRouter, Depends, HTTPException
from app.models.user import User
from app.services.auth_service import get_current_user
from app.services.json_utils import read_json, write_json

router = APIRouter()

@router.get("/admin/dashboard")
async def get_dashboard(current_user: User = Depends(get_current_user)):
    # Logic to retrieve data for the admin dashboard
    return {"message": "Welcome to the admin dashboard"}

@router.post("/admin/projects")
async def create_project(project_data: dict, current_user: User = Depends(get_current_user)):
    # Logic to create a new project
    projects = read_json("data/projects.json")
    # Add project creation logic here
    write_json("data/projects.json", projects)
    return {"message": "Project created successfully"}

@router.put("/admin/projects/{project_id}")
async def update_project(project_id: str, project_data: dict, current_user: User = Depends(get_current_user)):
    # Logic to update an existing project
    projects = read_json("data/projects.json")
    # Add project update logic here
    write_json("data/projects.json", projects)
    return {"message": "Project updated successfully"}

@router.delete("/admin/projects/{project_id}")
async def delete_project(project_id: str, current_user: User = Depends(get_current_user)):
    # Logic to delete a project
    projects = read_json("data/projects.json")
    # Add project deletion logic here
    write_json("data/projects.json", projects)
    return {"message": "Project deleted successfully"}
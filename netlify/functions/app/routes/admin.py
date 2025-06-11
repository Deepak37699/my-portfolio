from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/auth/login", response_class=HTMLResponse, name="admin_login")
async def admin_login(request: Request):
    """Admin login page."""
    templates = request.app.state.templates
    return templates.TemplateResponse("admin/login.html", {"request": request})

@router.get("/dashboard", response_class=HTMLResponse, name="admin_dashboard")
async def admin_dashboard(request: Request):
    """Admin dashboard page."""
    from app.services.data_manager import DataManager
    
    templates = request.app.state.templates
    data_manager = DataManager()
    
    # Get dashboard data
    projects = data_manager.get_all_projects()
    skills = data_manager.get_all_skills()
    messages = data_manager.get_all_messages()
    
    # Calculate stats
    stats = {
        "total_projects": len(projects),
        "featured_projects": len([p for p in projects if getattr(p, 'featured', False)]),
        "total_skills": len(skills),
        "total_messages": len(messages),
        "unread_messages": len([m for m in messages if not getattr(m, 'is_read', False)])
    }
    
    # Get recent messages (last 5)
    recent_messages = sorted(messages, key=lambda x: getattr(x, 'created_date', ''), reverse=True)[:5]
    
    # Mock user data (you might want to get this from session/auth)
    user = {"username": "admin"}
    
    context = {
        "request": request,
        "stats": stats,
        "recent_messages": recent_messages,
        "user": user
    }
    
    return templates.TemplateResponse("admin/dashboard.html", context)

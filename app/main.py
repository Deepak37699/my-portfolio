from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import os
import logging
from dotenv import load_dotenv

from app.routes import portfolio, admin, auth, debug
from app.services.json_utils import create_default_files

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title=os.getenv("APP_NAME", "FastAPI Portfolio"),
    description="Personal portfolio website built with FastAPI",
    version="1.0.0",
    docs_url="/docs" if os.getenv("DEBUG", "False").lower() == "true" else None,
    redoc_url="/redoc" if os.getenv("DEBUG", "False").lower() == "true" else None,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up static files
static_dir = Path(os.getenv("STATIC_DIR", "static"))
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Set up templates
templates_dir = Path(os.getenv("TEMPLATES_DIR", "templates"))
if templates_dir.exists():
    templates = Jinja2Templates(directory=str(templates_dir))
    
    # Make templates available to routes
    app.state.templates = templates

# Include routers
app.include_router(portfolio.router, tags=["Portfolio"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

@app.on_event("startup")
async def startup_event():
    """Initialize application on startup."""
    logger.info("Starting FastAPI Portfolio application...")
    
    # Create default JSON files if they don't exist
    try:
        create_default_files()
        logger.info("Default files initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing default files: {e}")
    
    logger.info("Application startup complete")

@app.on_event("shutdown")
async def shutdown_event():
    """Clean up on application shutdown."""
    logger.info("Shutting down FastAPI Portfolio application...")

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "FastAPI Portfolio is running"}

@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    """Custom 404 handler."""
    if hasattr(app.state, 'templates'):
        return app.state.templates.TemplateResponse(
            "404.html", 
            {"request": request}, 
            status_code=404
        )
    return {"detail": "Page not found"}

@app.exception_handler(500)
async def internal_error_handler(request: Request, exc):
    """Custom 500 handler."""
    logger.error(f"Internal server error: {exc}")
    if hasattr(app.state, 'templates'):
        return app.state.templates.TemplateResponse(
            "500.html", 
            {"request": request}, 
            status_code=500
        )
    return {"detail": "Internal server error"}

if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    debug = os.getenv("DEBUG", "False").lower() == "true"
    
    uvicorn.run(
        "app.main:app" if not debug else "app.main:app",
        host=host,
        port=port,
        reload=debug,
        log_level="info"
    )

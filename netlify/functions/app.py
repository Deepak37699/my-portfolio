import sys
import os
from pathlib import Path

# Add the current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Set environment variables for production
os.environ.setdefault("DEBUG", "False")
os.environ.setdefault("APP_NAME", "FastAPI Portfolio")
os.environ.setdefault("STATIC_DIR", str(current_dir.parent / "static"))
os.environ.setdefault("TEMPLATES_DIR", str(current_dir / "templates"))

# Change working directory to function directory
os.chdir(current_dir)

# Import the FastAPI app
from app.main import app
from mangum import Mangum

# Create the handler for Netlify Functions
handler = Mangum(app, lifespan="off", api_gateway_base_path="/")

def handler_function(event, context):
    return handler(event, context)

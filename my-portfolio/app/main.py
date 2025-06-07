from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.routes import portfolio, admin, auth

app = FastAPI()

# Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key="your_secret_key")

# Static files and templates setup
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Include routes
app.include_router(portfolio.router)
app.include_router(admin.router)
app.include_router(auth.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI Portfolio!"}
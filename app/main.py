"""Leave Management System - A web application that allows employees to apply for leave, managers to approve/reject requests, and HR to manage leave policies, balances, and reports."""
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from app.api.routes import router
from app.db.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Leave Management System",
    description="A web application that allows employees to apply for leave, managers to approve/reject requests, and HR to manage leave policies, balances, and reports.",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Include API routes
app.include_router(router, prefix="/api")

@app.get("/")
async def home(request: Request):
    """Render the home page"""
    return templates.TemplateResponse("index.html", {"request": request, "title": "Leave Management System"})

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "app": "Leave Management System"}

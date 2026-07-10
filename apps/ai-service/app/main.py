from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.api.v1.resume import router as resume_router

from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Career Intelligence AI Service",
    version="0.1.0",
)

app.include_router(health_router, prefix="/api/v1")
app.include_router(resume_router, prefix="/api/v1")
from fastapi import APIRouter
from .health import router as health
from .api.routes.upload import router as upload
from .api.routes.analyze import router as analyze
from .api.routes.report import router as report

api_router = APIRouter()
api_router.include_router(health, tags=["health"])
api_router.include_router(upload, prefix="/upload", tags=["upload"])
api_router.include_router(analyze, prefix="/analyze", tags=["analyze"])
api_router.include_router(report, prefix="/report", tags=["report"])

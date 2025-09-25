from fastapi import FastAPI
from .router import api_router

app = FastAPI(title="Resume Analyzer")
app.include_router(api_router, prefix="/api")

from typing import Optional, Dict, Any
from sqlmodel import SQLModel, Field
from datetime import datetime
from sqlalchemy import JSON  # 👈 مهم

class Resume(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class JobDescription(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    resume_id: str
    text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Analysis(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    resume_id: str
    jd_id: str
    # 👇 این سه‌تا قبلاً dict خالی بودن؛ الان به JSON مپ شدن
    scores: Dict[str, Any] = Field(default_factory=dict, sa_type=JSON)
    keywords: Dict[str, Any] = Field(default_factory=dict, sa_type=JSON)
    suggestions: Dict[str, Any] = Field(default_factory=dict, sa_type=JSON)
    created_at: datetime = Field(default_factory=datetime.utcnow)

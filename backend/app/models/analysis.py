from typing import Optional, Dict, Any
from sqlmodel import SQLModel, Field
from datetime import datetime
from sqlalchemy import JSON

class Analysis(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    resume_id: str
    jd_id: str
    scores: Dict[str, Any] = Field(default_factory=dict, sa_type=JSON)
    keywords: Dict[str, Any] = Field(default_factory=dict, sa_type=JSON)
    suggestions: Dict[str, Any] = Field(default_factory=dict, sa_type=JSON)
    created_at: datetime = Field(default_factory=datetime.utcnow)

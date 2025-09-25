from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class JobDescription(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    resume_id: str
    text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

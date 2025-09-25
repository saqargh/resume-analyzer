from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class Resume(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

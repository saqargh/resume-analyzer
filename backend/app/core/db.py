from sqlmodel import SQLModel, create_engine, Session
from pathlib import Path
import os

db_path = Path("backend/data/app.db")
db_path.parent.mkdir(parents=True, exist_ok=True)

DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{db_path}")
engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

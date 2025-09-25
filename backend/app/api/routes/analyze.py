import uuid
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import select
from ...core.db import get_session, init_db
from ...models import Resume, JobDescription, Analysis
from ...nlp.pipeline import analyze_resume_against_jd

router = APIRouter()

class AnalyzeIn(BaseModel):
    resume_id: str
    job_description: str

@router.post("")
def analyze(body: AnalyzeIn, session=Depends(get_session)):
    init_db()
    resume = session.get(Resume, body.resume_id)
    if not resume:
        raise HTTPException(404, "resume not found")
    jd = JobDescription(id=str(uuid.uuid4()), resume_id=resume.id, text=body.job_description)
    session.add(jd); session.commit()
    report = analyze_resume_against_jd(resume.text, jd.text)
    analysis = Analysis(
        id=str(uuid.uuid4()),
        resume_id=resume.id,
        jd_id=jd.id,
        scores=report.get("scores", {}),
        keywords=report.get("keywords", {}),
        suggestions=report.get("suggestions", {}),
    )
    session.add(analysis); session.commit()
    return {"analysis_id": analysis.id, "report": report}

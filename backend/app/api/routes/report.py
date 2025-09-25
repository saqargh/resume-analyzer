from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select, desc
from ...core.db import get_session, init_db
from ...models import Analysis

router = APIRouter()

@router.get("/{resume_id}")
def get_report(resume_id: str, session=Depends(get_session)):
    init_db()
    q = select(Analysis).where(Analysis.resume_id == resume_id).order_by(desc(Analysis.created_at))
    result = session.exec(q).first()
    if not result:
        raise HTTPException(404, "no analysis found for this resume")
    return {
        "analysis_id": result.id,
        "scores": result.scores,
        "keywords": result.keywords,
        "suggestions": result.suggestions,
        "created_at": result.created_at,
    }

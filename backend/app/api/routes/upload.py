import uuid
from fastapi import APIRouter, UploadFile, File, Depends
from sqlmodel import select
from ...core.db import get_session, init_db
from ...models import Resume

router = APIRouter()

@router.post("")
def upload_resume(file: UploadFile = File(...), session=Depends(get_session)):
    init_db()
    raw = file.file.read()
    # استخراج متن واقعی رو بعداً اضافه کن؛ فعلاً متن ساختگی:
    text = f"Uploaded file: {file.filename}\n\n" + raw[:2000].decode(errors="ignore")
    rid = str(uuid.uuid4())
    resume = Resume(id=rid, text=text)
    session.add(resume)
    session.commit()
    return {"resume_id": rid}

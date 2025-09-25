[README.md](https://github.com/user-attachments/files/22539406/README.md)
# Resume Analyzer

A production-ready web app that ingests resumes (PDF/DOCX), analyzes them with an NLP pipeline, scores strengths/weaknesses, extracts ATS keywords, and suggests improvements tailored to a target job description.

- Backend: FastAPI (Python 3.11), SQLModel (SQLite dev), NLP via spaCy, KeyBERT, sentence-transformers, scikit-learn
- Frontend: React + TypeScript + Vite + TailwindCSS, Zustand
- Tooling: pre-commit (black, isort, ruff), mypy, pytest, Playwright

## Ports
- API: http://localhost:8000 (OpenAPI docs at /docs)
- Web: http://localhost:5173

## Quickstart (local)

1) Backend

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
cp backend/.env.example backend/.env
uvicorn app.main:app --reload --app-dir backend
```

2) Frontend

```bash
cd frontend
npm install
npm run dev
```

3) Makefile shortcuts (from project root)

```bash
make dev    # backend + frontend concurrently
make api    # backend only
make web    # frontend only
make test   # backend tests
make e2e    # frontend e2e
```

## Environment

Create `backend/.env` from example:

```env
DATABASE_URL=sqlite:///./data/app.db
LLM_ENABLE=false
OPENAI_API_KEY=
HUGGINGFACE_HUB_TOKEN=
REDIS_URL=redis://redis:6379/0
CORS_ORIGINS=http://localhost:5173
```

## Sample cURL

Upload a resume (PDF/DOCX):

```bash
curl -X POST "http://localhost:8000/api/upload" \
  -F "file=@data/samples/resume_sample.pdf" \
  -F "pii_scrub=true"
```

Run analysis:

```bash
curl -X POST "http://localhost:8000/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"resume_id": "<UUID>", "job_description": "We seek a Python backend engineer..."}'
```

Fetch latest report:

```bash
curl http://localhost:8000/api/report/<UUID>
```

## Docker Compose

```bash
docker compose up --build
```

## Screenshots / GIFs

- Add screenshots of Upload, Analyze, and Report pages here.

## Notes

- The NLP pipeline falls back to heuristic scoring if heavy models are unavailable. Enable richer suggestions with `LLM_ENABLE=true` and API keys.
- Structure anticipates future auth and PostgreSQL.

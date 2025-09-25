def analyze_resume_against_jd(resume_text: str, jd_text: str) -> dict:
    # نسخه دم‌دستی برای راه افتادن؛ بعداً حرفه‌ایش می‌کنیم
    must = []
    for kw in ["Python","FastAPI","Docker","SQL","NLP","LLM"]:
        if kw.lower() in jd_text.lower() and kw.lower() not in resume_text.lower():
            must.append(kw)
    score = 0.6 + min(0.4, len(set(resume_text.split()) & set(jd_text.split()))/100)
    return {
        "scores": {"match": round(score, 2), "skills": 0.65, "experience": 0.7},
        "keywords": {"must_have": must, "nice_to_have": ["CI/CD","Kubernetes"]},
        "suggestions": [
            "دستاوردها رو عددی کن (مثلاً latency رو 30% کم کردم).",
            "کلیدواژه‌های JD رو به رزومه اضافه کن: " + ", ".join(must) if must else "اوکی‌ای!"
        ],
    }

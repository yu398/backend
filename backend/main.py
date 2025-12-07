# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Internship API - Mock")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status":"Server OK","message":"Internship API (mock) running"}

@app.get("/jobs")
def jobs(limit: int = 10, offset: int = 0, q: str = None):
    sample = [
        {"id":1,"title":"資料分析實習生","company":"數據坊","location":"遠端"},
        {"id":2,"title":"前端實習生","company":"XYZ 新創","location":"台北"}
    ]
    return {"count": len(sample), "jobs": sample}

@app.post("/like")
def like(payload: dict):
    return {"ok": True, "payload": payload}

@app.post("/match")
def match(payload: dict):
    return {"user_id": payload.get("user_id"), "matches":[{"job_id":1,"score":0.89,"title":"資料分析實習生","company":"數據坊"}]}

# Optional: simple health route for readiness checks
@app.get("/health")
def health():
    return {"status":"ok"}

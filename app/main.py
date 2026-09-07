from fastapi import FastAPI
from pydantic import BaseModel, Field

from .analyzer import analyze_event

app = FastAPI(
    title="SecureDeploy Security Monitor",
    version="1.0.0",
    description="Educational defensive API for analyzing synthetic security events.",
)


class EventRequest(BaseModel):
    event: str = Field(min_length=3, max_length=1000)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "securedeploy"}


@app.post("/analyze")
def analyze(request: EventRequest) -> dict:
    findings = analyze_event(request.event)
    return {
        "event": request.event,
        "finding_count": len(findings),
        "findings": [finding.__dict__ for finding in findings],
    }

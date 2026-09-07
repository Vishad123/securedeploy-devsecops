# SecureDeploy — DevSecOps Security Monitor

SecureDeploy is an educational DevSecOps/CloudOps project that packages a small Python security-event API with Docker and GitHub Actions.

## What it demonstrates

- Python REST API for defensive security-event analysis
- Docker containerization
- Automated unit tests
- CI workflow with lint/test checks
- Dependency and container security scanning
- Health checks and structured JSON responses
- Security-minded configuration using environment variables

## Architecture

Client → FastAPI → Security Event Analyzer
                 ↓
          JSON security findings

CI: GitHub Actions → tests → dependency scan → container build

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs`.

## Run with Docker

```bash
docker build -t securedeploy .
docker run --rm -p 8000:8000 securedeploy
```

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Example analysis request:

```bash
curl -X POST http://127.0.0.1:8000/analyze   -H "Content-Type: application/json"   -d '{"event":"failed login from 203.0.113.10 for admin"}'
```

## Testing

```bash
python -m unittest discover -s tests -v
```

## Security note

The project uses synthetic/example security events and documentation-only IP addresses. It is intended for defensive learning, DevSecOps practice, and portfolio demonstration.

## Portfolio skills

**Python • FastAPI • Docker • GitHub Actions • DevSecOps • CloudOps concepts • REST APIs • Automated testing • Security scanning**

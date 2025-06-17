# app/

This directory contains the sample FastAPI web application for the DevSecOps CI/CD pipeline demo.

## Features
- `/health` endpoint for health checks
- `/logs` endpoint for recent application logs (last 50 lines)
- `/metrics` endpoint for Prometheus-compatible metrics (request count, error count, uptime)
- Pinned dependencies in `requirements.txt`
- Secure, multi-stage Dockerfile (non-root user)
- Example unit test in `tests/`

## Code Quality Requirements
- Linting: `flake8` (no errors/warnings allowed)
- Formatting: `black` (must be formatted)
- Import sorting: `isort` (must be sorted)
- Test coverage: `pytest-cov` (minimum 80% required)

## Usage

### Local Development
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### Run Tests
```bash
pip install pytest
pytest tests/
```

### Build & Run with Docker
```bash
docker build -t devsecops-app .
docker run -p 8000:8000 devsecops-app
```

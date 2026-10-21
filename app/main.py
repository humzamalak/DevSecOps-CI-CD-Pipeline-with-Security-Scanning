import logging
import os
import time
from logging.handlers import RotatingFileHandler

import uvicorn
from fastapi import FastAPI, Request
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Gauge, generate_latest
from starlette.responses import JSONResponse, PlainTextResponse

app = FastAPI(title="Sample DevSecOps App")

# Logging setup
LOG_FILE = os.environ.get("LOG_FILE", "app.log")
logger = logging.getLogger("devsecops-app")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(LOG_FILE, maxBytes=1000000, backupCount=3)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
if not logger.hasHandlers():
    logger.addHandler(handler)

# Prometheus metrics
REQUEST_COUNT = Counter(
    "app_requests_total", "Total HTTP requests", ["method", "endpoint"]
)
ERROR_COUNT = Counter("app_errors_total", "Total error responses", ["endpoint"])
UPTIME = Gauge("app_uptime_seconds", "Seconds since the app started")
START_TIME = time.time()


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    endpoint = request.url.path
    method = request.method
    REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        ERROR_COUNT.labels(endpoint=endpoint).inc()
        logger.error(f"Error on {endpoint}: {e}")
        raise


@app.get("/health", tags=["Health"])
def health_check():
    logger.info("Health check called")
    return JSONResponse({"status": "ok"})


@app.get("/logs", tags=["Monitoring"])
def get_logs():
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()[-50:]
        return PlainTextResponse("".join(lines), media_type="text/plain")
    except Exception as e:
        logger.error(f"Failed to read logs: {e}")
        return PlainTextResponse("Log file not found or unreadable.", status_code=404)


@app.get("/metrics", tags=["Monitoring"])
def metrics():
    # Uptime metric
    UPTIME.set(time.time() - START_TIME)
    metrics_output = generate_latest()
    return PlainTextResponse(metrics_output, media_type=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

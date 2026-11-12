# syntax=docker/dockerfile:1
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
# Write logs to /tmp so the app runs as non-root and with a read-only root filesystem
ENV LOG_FILE=/tmp/app.log
EXPOSE 8000
# Numeric non-root UID (>= 10000) so Kubernetes runAsNonRoot can verify it
USER 10001:10001
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

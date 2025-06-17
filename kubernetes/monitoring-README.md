# Monitoring & Alerting for DevSecOps App

## Overview
This setup uses Prometheus and Grafana (via Helm) to monitor the FastAPI app and cluster.

## Prometheus
- Scrapes `/metrics` endpoint from the app (see `prometheus-values.yaml`).
- Alert rules in `prometheus-alerts.yaml`:
  - **AppDown**: No metrics received for 1 minute.
  - **HighErrorRate**: More than 5 errors in 5 minutes.

## Grafana
- Deploy with `grafana-values.yaml` for basic setup.
- Add Prometheus as a data source.
- Create dashboards for request count, error rate, and resource usage.

## Deployment
1. Install Prometheus:
   ```bash
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm install prometheus prometheus-community/prometheus -f kubernetes/prometheus-values.yaml
   ```
2. Install Grafana:
   ```bash
   helm repo add grafana https://grafana.github.io/helm-charts
   helm install grafana grafana/grafana -f kubernetes/grafana-values.yaml
   ```
3. Apply alert rules:
   ```bash
   kubectl apply -f kubernetes/prometheus-alerts.yaml
   ```

## Alerting
- Integrate Prometheus Alertmanager with Slack/email for notifications.
- Customize alert rules as needed for your environment.

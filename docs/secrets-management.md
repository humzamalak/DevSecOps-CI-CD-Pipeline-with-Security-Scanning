# Secrets Management & Rotation

## Overview
This project uses AWS Secrets Manager and Kubernetes External Secrets for secure secret management.

- **No secrets are stored in code or Docker images.**
- All sensitive values (e.g., SUPABASE_URL, SUPABASE_KEY) are referenced via ExternalSecret resources.
- GitHub Actions and Kubernetes workloads use secrets from AWS Secrets Manager.

## How it Works
- Secrets are stored in AWS Secrets Manager under keys like `devsecops-app/supabase-url`.
- The `ExternalSecret` resource syncs these secrets into Kubernetes as native secrets.
- The app loads secrets from environment variables (injected from Kubernetes secrets).

## Secret Rotation
- Rotate secrets in AWS Secrets Manager as needed.
- ExternalSecret will automatically update the Kubernetes secret on the next sync.
- Update GitHub Actions secrets via the repository settings.

## Validation
- Trivy and Gitleaks scan for secrets in code and images.
- CI/CD pipeline fails if secrets are detected in code.

## Exception Process
- For emergency or temporary secrets, document the reason, approver, and expiration in a `security-exception.yaml` (see container security docs).

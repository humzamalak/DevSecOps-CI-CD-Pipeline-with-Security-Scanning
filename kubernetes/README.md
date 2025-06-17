# Kubernetes Manifests for DevSecOps App

This directory contains Kubernetes manifests for deploying the DevSecOps sample application.

## Files
- `deployment.yaml`: Secure deployment for the FastAPI app, referencing signed images from ECR.
- `service.yaml`: ClusterIP service exposing the app on port 80.
- `ingress.yaml`: Ingress resource for external access (update host as needed).
- `image-policy.yaml`: OPA Gatekeeper policy enforcing signed images.

## Security Best Practices
- Uses non-root user, disables privilege escalation, and enforces read-only root filesystem.
- Resource requests and limits are set for CPU and memory.
- Reference only signed images from your ECR registry.
- Use `imagePullSecrets` if your ECR is private.
- Enforce signature verification with Gatekeeper.

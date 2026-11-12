# Kubernetes Manifests for DevSecOps App

This directory contains Kubernetes manifests for deploying the DevSecOps sample application.

## Files
- `namespace.yaml`: `devsecops` namespace with the labels the Gatekeeper namespace policy requires.
- `serviceaccount.yaml`: dedicated ServiceAccount with no API token mounted.
- `networkpolicy.yaml`: allows ingress to the app only on port 8000 from `ingress-nginx` and `monitoring`.
- `deployment.yaml`: Secure deployment for the FastAPI app, referencing signed images from ECR.
- `service.yaml`: ClusterIP service exposing the app on port 80.
- `ingress.yaml`: Ingress resource for external access (update host as needed).
- `image-policy.yaml`: OPA Gatekeeper constraint enforcing signed images (needs the `K8sRequiredSignatures` ConstraintTemplate from `policies/gatekeeper/templates/require-signed-images.yaml`). The template is a placeholder: it does not verify Cosign signatures yet.

## Security Best Practices
- Uses non-root user, disables privilege escalation, and enforces read-only root filesystem.
- Resource requests and limits are set for CPU and memory.
- Reference only signed images from your ECR registry.
- Use `imagePullSecrets` if your ECR is private.
- Signature verification at admission is not implemented yet. Use a verifier such as Sigstore policy-controller or Kyverno `verifyImages` to add it.

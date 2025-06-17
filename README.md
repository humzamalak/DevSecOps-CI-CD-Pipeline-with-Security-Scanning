# DevSecOps CI/CD Pipeline

![CI](https://github.com/${{github.repository}}/actions/workflows/build.yml/badge.svg?branch=main)

This repository implements a secure, production-grade CI/CD pipeline with integrated security scanning, containerization, and Kubernetes orchestration.

## Documentation

- [Container Security & Supply Chain Attestation](docs/container-security.md)

## Structure

- `app/` — Sample Python web application
- `kubernetes/` — Kubernetes manifests
- `terraform/` — Infrastructure as code
- `security/` — Security policies and config
- `.github/` — GitHub Actions workflows and config
- `docs/` — Documentation and runbooks

See `docs/` for more details.
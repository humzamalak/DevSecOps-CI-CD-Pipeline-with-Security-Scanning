# Security & Quality Gates

This repository enforces security and code quality at every stage of the CI/CD pipeline.

## Automated Security Scanning

- **Semgrep (SAST):**  
  Scans all Python application code for security vulnerabilities and code quality issues.  
  - Fails the build on high/critical findings.
  - Results are uploaded to the GitHub Security tab (see "Code scanning alerts").

- **Checkov (IaC):**  
  Scans all Terraform and Kubernetes manifests for misconfigurations and policy violations.  
  - Fails the build on critical findings.
  - Output is visible in the Actions workflow logs.

- **Trivy (Container):**  
  Scans Dockerfiles and built images for vulnerabilities and license issues.  
  - Fails the build on critical vulnerabilities.

## Code Quality Gates

- **flake8:** No linting errors or warnings allowed.
- **black:** All code must be formatted.
- **isort:** All imports must be sorted.
- **pytest-cov:** Minimum 80% test coverage required.

## How to Fix Issues

- Review the "Actions" tab for failed jobs and logs.
- For code scanning alerts, visit the "Security" tab.
- Fix issues locally, re-run checks, and push updates.

## References

- [Container Security & Supply Chain Attestation](docs/container-security.md)
- [GitHub Security Tab](../../security/code-scanning)
- [GitHub Actions](../../actions) 
# Security & Quality Gates

This repository enforces security and code quality at every stage of the CI/CD pipeline.

## Automated Security Scanning

Defined in `.github/workflows/build.yml` (every push and pull request to `main`)
and `.github/workflows/security.yml` (daily).

- **Semgrep (SAST):** scans `app/` with the `auto` rule set. Any finding fails
  the build. Results are uploaded to the Security tab ("Code scanning alerts").
- **Gitleaks (secrets):** scans the full Git history. Any finding fails the build.
- **Checkov (IaC):** scans `terraform/` and `kubernetes/`. Any failed check
  fails the build. Accepted exceptions are skipped in the file itself with a
  written reason: `CKV_TF_1` on the two registry modules (pinned to an exact
  version) and `CKV_K8S_43` on the Deployment (commit-SHA tag set at deploy).
- **Trivy (container):** the Dockerfile configuration scan fails the build on
  HIGH or CRITICAL findings. The image vulnerability scan reports HIGH and
  CRITICAL issues with a fix available, but does not fail the build.
- **OPA Gatekeeper (policy):** `gator verify` runs unit tests for the
  Gatekeeper policies in `kubernetes/policies/gatekeeper/`. A failed test fails
  the build.
- **SBOM:** Syft writes a CycloneDX SBOM of the image as a build artefact.

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
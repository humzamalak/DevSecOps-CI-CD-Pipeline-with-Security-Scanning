# Container Security and Supply Chain

This document describes what the pipeline does to secure the container image,
and what it does not do yet. The steps are in `.github/workflows/build.yml`.

## What runs on every build

| Step | Tool | Result |
| --- | --- | --- |
| Dockerfile configuration scan | Trivy (`config`) | HIGH or CRITICAL findings fail the build |
| Image build | Docker Buildx | Single-arch image, loaded locally for the next steps |
| Image vulnerability scan | Trivy (`image`) | Reports HIGH and CRITICAL issues that have a fix; does not fail the build |
| SBOM | Syft (CycloneDX JSON) | `sbom.cdx.json`, stored as a build artefact |

## What runs on `main` when AWS is enabled

These steps run only when the repository variable `AWS_DEPLOY_ENABLED` is
`true` (see the README).

1. Push a `linux/amd64` and `linux/arm64` image to Amazon ECR, tagged with the
   commit SHA. The ECR repository has immutable tags, so a tag cannot be
   overwritten.
2. Sign the image digest with Cosign keyless signing. The GitHub OIDC token
   proves the workflow identity, Fulcio issues a short-lived certificate, and
   the signature is recorded in the Rekor transparency log.
3. Attach the SBOM to the image as a Cosign attestation (`--type cyclonedx`).
   The SBOM describes the `linux/amd64` image that was built and scanned.
4. Create a build provenance attestation with
   `actions/attest-build-provenance` and push it to the registry.

## Image hardening

From `app/Dockerfile` and `kubernetes/deployment.yaml`:

- Multi-stage build on `python:3.11-slim`.
- Runs as UID 10001, with `runAsNonRoot: true` and the RuntimeDefault seccomp profile.
- All Linux capabilities dropped, `allowPrivilegeEscalation: false` and `readOnlyRootFilesystem: true`; logs
  go to an `emptyDir` volume on `/tmp`.
- CPU and memory requests and limits are set.

## Verify an image by hand

Replace the registry, account and digest with your own values.

```bash
# Signature
cosign verify \
  --certificate-identity-regexp "https://github.com/humzamalak/DevSecOps-CI-CD-Pipeline-with-Security-Scanning" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
  <account>.dkr.ecr.us-east-1.amazonaws.com/devsecops-app@sha256:<digest>

# SBOM attestation
cosign verify-attestation --type cyclonedx \
  --certificate-identity-regexp "https://github.com/humzamalak/DevSecOps-CI-CD-Pipeline-with-Security-Scanning" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
  <account>.dkr.ecr.us-east-1.amazonaws.com/devsecops-app@sha256:<digest>

# Build provenance
gh attestation verify \
  oci://<account>.dkr.ecr.us-east-1.amazonaws.com/devsecops-app@sha256:<digest> \
  --repo humzamalak/DevSecOps-CI-CD-Pipeline-with-Security-Scanning
```

## Not implemented yet

- **Signature verification at admission.** The Gatekeeper template
  `kubernetes/policies/gatekeeper/templates/require-signed-images.yaml` is a
  placeholder: it matches a fixed digest suffix and does not check Cosign
  signatures. A cluster can therefore run an unsigned image. To close this gap,
  add Sigstore policy-controller or Kyverno `verifyImages`.
- **Blocking on image vulnerabilities.** The Trivy image scan reports only.
- **Enforcing Gatekeeper policies.** All constraints use
  `enforcementAction: dryrun`, so they audit and do not block.

## References

- [Cosign](https://docs.sigstore.dev/cosign/overview/)
- [SLSA](https://slsa.dev/)
- [GitHub artifact attestations](https://docs.github.com/en/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds)
- [OPA Gatekeeper](https://open-policy-agent.github.io/gatekeeper/)

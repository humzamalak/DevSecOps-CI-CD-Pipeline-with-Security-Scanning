# Gatekeeper Policies

This directory contains OPA Gatekeeper constraint templates and constraints for EKS.

- `templates/`: ConstraintTemplates (Rego). Apply these first.
- `constraints/`: one constraint per template. Apply after Gatekeeper has created the CRDs.
- `tests/`: `gator verify` test suite, run in CI by the `policy` job.

Run the tests locally:

```bash
gator verify kubernetes/policies/gatekeeper/tests/
```

The policies check Pods (and Namespaces for labels). Gatekeeper evaluates the
Pods that Deployments create, so the Deployment itself is not checked directly.

## Baseline Policies (Audit Mode)
- Require signed images (placeholder: matches a fixed digest suffix and does not verify Cosign signatures)
- Restrict privilege escalation
- Enforce namespace labels
- Restrict HostPath/HostNetwork
- Enforce resource requests/limits
- Block default ServiceAccount usage

## Usage
- All constraints use `enforcementAction: dryrun` (audit only). Review violations in Prometheus/Grafana before enforcing.
- See below for install and monitoring instructions.

## Install/Upgrade Gatekeeper (Helm)
```bash
helm repo add gatekeeper https://open-policy-agent.github.io/gatekeeper/charts
helm upgrade --install gatekeeper gatekeeper/gatekeeper \
  --namespace gatekeeper-system --create-namespace
```

## Monitoring & Alerting
- Gatekeeper exposes metrics on `/metrics` (port 8888).
- Prometheus scrapes these metrics; see `prometheus-values.yaml`.
- Example alert rules and Grafana dashboard JSON are provided in this repo.

## References
- [Gatekeeper Policy Library](https://github.com/open-policy-agent/gatekeeper-library)
- [Gatekeeper Docs](https://open-policy-agent.github.io/gatekeeper/)

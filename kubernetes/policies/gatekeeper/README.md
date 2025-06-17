# Gatekeeper Policies

This directory contains OPA Gatekeeper constraint templates and constraints for EKS.

## Baseline Policies (Audit Mode)
- Require signed images
- Restrict privilege escalation
- Enforce namespace labels
- Restrict HostPath/HostNetwork
- Enforce resource requests/limits
- Block default ServiceAccount usage

## Usage
- All policies are applied in audit mode first. Review violations in Prometheus/Grafana before enforcing.
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

# Terraform Infrastructure for DevSecOps CI/CD

This directory provisions AWS EKS infrastructure using Terraform.

## Files
- `main.tf`: Core resources (VPC, EKS cluster, node groups)
- `variables.tf`: Input variables for customization
- `outputs.tf`: Useful outputs (cluster name, kubeconfig, VPC ID)

## Usage

1. Install [Terraform](https://www.terraform.io/downloads.html)
2. Initialize the working directory:
   ```bash
   terraform init
   ```
3. Review and customize variables in `variables.tf` as needed.
4. Plan the deployment:
   ```bash
   terraform plan
   ```
5. Apply the configuration:
   ```bash
   terraform apply
   ```

## Security Best Practices
- Uses official AWS modules for VPC and EKS
- Enables IAM Roles for Service Accounts (IRSA)
- Private subnets for worker nodes
- Resource limits and RBAC recommended in Kubernetes manifests

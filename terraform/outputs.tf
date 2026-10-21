output "cluster_name" {
  description = "EKS cluster name"
  value       = module.eks.cluster_name
}

output "cluster_endpoint" {
  description = "EKS cluster API endpoint (use `aws eks update-kubeconfig` to build a kubeconfig)"
  value       = module.eks.cluster_endpoint
}

output "vpc_id" {
  description = "VPC ID"
  value       = module.vpc.vpc_id
}

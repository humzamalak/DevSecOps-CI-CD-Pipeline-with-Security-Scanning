output "cluster_name" {
  description = "EKS cluster name"
  value       = module.eks.cluster_name
}

output "kubeconfig" {
  description = "Kubeconfig file content"
  value       = module.eks.kubeconfig
}

output "vpc_id" {
  description = "VPC ID"
  value       = module.vpc.vpc_id
}

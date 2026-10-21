# Main Terraform configuration for EKS (AWS)

terraform {
  required_version = ">= 1.3"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.40"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

module "vpc" {
  source             = "terraform-aws-modules/vpc/aws"
  version            = "5.1.0"
  name               = "devsecops-vpc"
  cidr               = var.vpc_cidr
  azs                = ["${var.aws_region}a", "${var.aws_region}b"]
  private_subnets    = var.private_subnets
  public_subnets     = var.public_subnets
  enable_nat_gateway = true
  single_nat_gateway = true
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "20.8.4"
  cluster_name    = var.cluster_name
  cluster_version = "1.29"
  subnet_ids      = module.vpc.private_subnets
  vpc_id          = module.vpc.vpc_id
  enable_irsa     = true
  eks_managed_node_groups = {
    default = {
      desired_size   = 2
      max_size       = 3
      min_size       = 1
      instance_types = ["t3.medium"]
    }
  }
}

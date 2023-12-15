terraform {
  backend "s3" {
    key    = "terraform/states/graphql_backend_api"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.67.0"
    }
  }

  required_version = "~> 1.2"
}
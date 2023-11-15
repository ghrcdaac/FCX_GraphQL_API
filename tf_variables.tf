## variables for aws provider
variable "aws_creds_path" {
  description = "The path to aws credentials file"
  type    = string
  default = "~/.aws/credentials"
}

variable "aws_region" {
  description = "AWS region for all resources."
  type    = string
}


## Ones with default values. Placed to easily manipulate these

variable "key_name" {
  description = "PEM key to ssh into instance."
  type    = string
  default = "key.pem"
}

variable "instance_type" {
  description = "The type of instance to start."
  type = string
  default = "t3.micro"
}
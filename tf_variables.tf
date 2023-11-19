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

variable "accountId" {
  description = "AWS account id."
  type    = string
}

#

variable "POSTGRES_DB" {
  description = "used for postgres db initialization and used by Django API"
  type = string
}

variable "POSTGRES_USER" {
  description = "used for postgres db initialization and used by Django API"
  type = string
}

variable "POSTGRES_PASSWORD" {
  description = "used for postgres db initialization and used by Django API"
  type = string
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
  default = "t2.micro"
}
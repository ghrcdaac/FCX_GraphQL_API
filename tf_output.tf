// Output
output "public_ip" {
  value = aws_instance.fcx_backend_graphql_api.public_ip
}

output "private_pem" {
  value = tls_private_key.rsa_4096.private_key_pem
  sensitive = true
}
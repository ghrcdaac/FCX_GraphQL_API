#! /bin/bash
set -e
sudo yum update -y

# docker install
sudo amazon-linux-extras install docker -y
sudo service docker start
usermod -a -G docker ec2-user

# creds helper, to get images from ecr into ec2 using premissions granted by role
sudo yum install amazon-ecr-credential-helper -y
echo '{"credsStore": "ecr-login"}' > ~/.docker/config.json

# login to aws ecr
# export aws_region="${aws_region}" accountId="${accountId}"
aws --region ${aws_region} ecr get-authorization-token
aws ecr get-login-password --region ${aws_region} | docker login --username AWS --password-stdin ${accountId}.dkr.ecr.${aws_region}.amazonaws.com

sleep 2

docker pull ${accountId}.dkr.ecr.${aws_region}.amazonaws.com/fcx-backend-api:latest
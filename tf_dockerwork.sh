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

docker run -d -p 80:5000 {account_id}.dkr.ecr.{region}.amazonaws.com/fcx-backend-api:latest

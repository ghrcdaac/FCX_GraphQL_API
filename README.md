# FCX BACKEND API

This repository contains the code and instructions for setting up the FCX Backend API with GraphQL to access Field Campaign's layer data.

## Steps to Get Started in Local

Follow these steps to set up and run the FCX Backend API. Docker is recommended for simplicity.

### Prerequisites

- Docker installed on your system

### Setup Environment

Using the `.env.example` file as a reference, create `.env` in the project root directory. The values set for the database will be used to create user in Postgres, as well as, connect to the database from the Django API.

### 1. Build Docker Images

Run the following command to build the Docker images required for the application:

```bash
docker-compose build
```

### 2. Start the Application

Start the application by running the following command:

```bash
docker-compose up
```

### 3. Migrate the Database (if needed)

If you are running the application for the first time or if the database model has changed, apply the migrations using:

```bash
docker-compose run api python manage.py migrate
```

### 4. Load the Seed Data (if needed)

If you are running the application for the first time and need to add seed data, use the following command:

```bash
docker-compose run api python manage.py loaddata HS3_campaign_seed
```

### 5. Set Up Django Admin

To access the Django admin panel, we need to first create superuser. Run the following command and follow the prompts to create a superuser account:

```bash
docker-compose run api python manage.py createsuperuser
```

## Accessing the Application

- The GraphQL API is available at: [http://localhost:8000/graphql](http://localhost:8000/graphql)
- The Django admin panel is accessible at: [http://localhost:8000/admin](http://localhost:8000/admin)
- The database admin panel can be accessed through: [http://localhost:8009](http://localhost:8009)

Feel free to explore and interact with the FCX Backend GraphQL application using these URLs. If you encounter any issues or have questions, please refer to the documentation or reach out to the development team.

## GRAPHQL Example:
Use the following query to get desired layer data. 
```
query {
  campaignLayerByName(name: "HS3") {
    title
    logoUrl
    description
    links {
      title
      url
    }
    dois {
      longName
      instrumentShortName
      url
    }
    legends {
      instrumentShortName
      url
      color
    }
    instrumentlayers {
      layerId
      date
      instrumentShortName
      displayName
      displayMechanism
      type
      platform
      url
      unit
      addTickEventListner
      variableName
      fieldCampaignName
    }
  }
}

```

## Steps to Deploy in AWS infrastrucutre

### Prerequisites

- Docker installed on your system
- Terraform installed on your system

Follow these steps to deploy the FCX Backend API in the AWS infrastructure.

### 1.  Export necessary env variables:
  ```
   export
   TF_VAR_aws_region="xxxxxxxxxx"
   TF_VAR_accountId="xxxxxxxxxx"
   TF_VAR_S3_STATE_BUCKET="xxxxxxxxxx"
   TF_VAR_S3_STATE_BUCKET_aws_region="xxxxxxxxxx"
   TF_VAR_POSTGRES_DB="xxxxxxxxxx"
   TF_VAR_POSTGRES_USER="xxxxxxxxxx"
   TF_VAR_POSTGRES_PASSWORD="xxxxxxxxxx"
   ```

  - `TF_VAR_aws_region`, `TF_VAR_accountId` is used for AWS EC2 infrastructure creation.
  - `TF_VAR_S3_STATE_BUCKET` is used for terraform state management i.e. to maintain consistent deployment across multiple devices while using terraform. `TF_VAR_S3_STATE_BUCKET_aws_region` is the region where the state bucket is in.
  - `TF_VAR_POSTGRES_DB` is the name of the postgres database, `TF_VAR_POSTGRES_USER` is the user name of the postgres database, and `TF_VAR_POSTGRES_PASSWORD` is the password for the particular user. These database configuration are both used by the postgres database docker image and the FCX (django) backend GraphQL API.

### 2. Deploy the infrastructure.

At the root directory of the project, run the following command:
```bash
bash ./deploy.sh
```

This deployment shell script runs in two parts.
  - `predeploy.sh` is invoked initially. Here, a docker image is generated from the available code and the docker image is pushed to AWS ECR.
  - `terraform apply` is then invoked. Here, terraform scripts are used in unison to create resources in AWS. Firstly, EC2 instance with predefined configuration is created, secondly, the infrastructure is bootstrapped with necessary packages, and then the appropriate docker images are pulled and are started with necessary environment variables.

### 3. Use the outputs

The terraform script will put out some outputs.
  - `key.pem`
  - Public IP of the EC2 infrastructure.

The EC2 instance can be accessed using the private `key.pem`, i.e. using the following command:
  ```
  ssh -i ./key.pem ec2-user@<public_ip>
  ```

Also, to access the FCX backend GraphQL API, use `https://<ip>/graphql/`
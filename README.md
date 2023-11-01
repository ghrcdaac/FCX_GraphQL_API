# FCX BACKEND API

This repository contains the code and instructions for setting up the FCX Backend API with GraphQL to access Field Campaign's layer data.

## Steps to Get Started

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
      addTickEventListener
      variableName
      fieldCampaignName
    }
  }
}

```

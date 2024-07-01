# FastAPI Blog Project

This is a simple CRUD blog application built with FastAPI, PostgreSQL, SQLAlchemy, Alembic, and Docker.

## Setup and Running

### Prerequisites

- Docker
- Docker Compose
- pgAdmin (optional, for database management)

### Environment Variables

Create  `.env` file and copy variables from `.env.example`.

### Clone the Repository

```
git clone https://github.com/nedoder/fastapi-blog.git
```

```
cd fastapi-blog
```

### Build and Start Docker Containers

```
docker-compose up --build
```

### Build and Start Docker Containers

```
docker-compose exec web alembic upgrade head
```

### Access the Application

Open your browser and navigate to http://localhost:8000 to access the FastAPI application
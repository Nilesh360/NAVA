# 🏢 Organization Management API

A scalable and modular FastAPI project to manage organizations dynamically. Each organization has its own database, and admins can log in to manage their resources securely using JWT authentication.

---

## Features

- ✅ Create organizations with unique dynamic databases
- ✅ Register admin users during organization creation
- ✅ Store organization metadata in a master database
- ✅ Admin login with JWT token authentication
- ✅ Modular FastAPI structure for scalability
- ✅ Dockerized for container-based deployment
- ✅ Swagger & ReDoc documentation with custom paths

---

## Project Structure
NAVA
├── src/
|   ├── api/
|   │    ├── routers/ # API routes
|   │    ├── service/ # DB CRUD logic
|   │    ├── database/ # DB setup & handlers
|   │    ├── models/ # SQLAlchemy models
|   │    └── view_schemas/ # Pydantic schemas
|   ├── app.py # App entrypoint
|   ├── common/security # Security & config
|   └── requirements.txt
├── deployments
|       └── DockerFile
└── README.md




## Install & Run

1. Install Locally

```
git clone <your-repo>
cd organization_service
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

2. Access Documentation
Swagger: http://127.0.0.1:8000/docs

3. Command to run locally
uvicorn src.app:app --reload --port 8000



## 🧑‍💻 Author
Nilesh Gupta
Backend Developer
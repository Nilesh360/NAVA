from fastapi import FastAPI
from src.api.routers import organization, auth

app = FastAPI(
    title="Organization Management API",
    description="APIs to manage organizations, admin login, and dynamic databases",
    version="1.0.0"
    )

app.include_router(organization.router, prefix="/org",tags=["Organization"])
app.include_router(auth.router, prefix="/admin",tags=["Auth"])



from fastapi import APIRouter, HTTPException
from src.api.view_schemas.organization import OrgCreate, OrgOut
from src.api.services.master_db import create_org_in_master, get_org_by_name
from src.api.database.dynamic_db_handler import create_dynamic_db_with_admin

router = APIRouter()

@router.post("/create", response_model=OrgOut)
def create_organization(org: OrgCreate):
    if get_org_by_name(org.organization_name):
        raise HTTPException(status_code=400, detail="Organization already exists")
    db_info = create_dynamic_db_with_admin(org)
    created = create_org_in_master(org.organization_name, db_info)
    return created

@router.get("/get", response_model=OrgOut)
def get_organization(name: str):
    org = get_org_by_name(name)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org
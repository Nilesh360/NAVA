from pydantic import BaseModel

class OrgCreate(BaseModel):
    email: str
    password: str
    organization_name: str

class OrgOut(BaseModel):
    organization_name: str
    db_url: str
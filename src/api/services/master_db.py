from sqlalchemy.orm import Session
from src.api.models.master import Organization
from src.api.database.master import SessionLocal

def create_org_in_master(name, db_url):
    db: Session = SessionLocal()
    org = Organization(organization_name=name, db_url=db_url)
    db.add(org)
    db.commit()
    db.refresh(org)
    db.close()
    return org

def get_org_by_name(name):
    db: Session = SessionLocal()
    org = db.query(Organization).filter(Organization.organization_name == name).first()
    db.close()
    return org
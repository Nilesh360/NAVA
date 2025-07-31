import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.api.models.dynamic import AdminUser
from src.common.security import get_password_hash
from src.api.database.base import Base

def create_dynamic_db_with_admin(org):
    db_url = f"sqlite:///./{org.organization_name}.db"
    engine = create_engine(db_url, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    user = AdminUser(email=org.email, hashed_password=get_password_hash(org.password))
    db.add(user)
    db.commit()
    db.close()
    return db_url

def get_dynamic_session(email):
    # In real-case, map email to organization/db_url using master DB
    db_url = f"sqlite:///./{email.split('@')[0]}.db"
    engine = create_engine(db_url, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()
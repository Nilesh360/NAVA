from sqlalchemy import Column, Integer, String
from src.api.database.master import Base

class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True, index=True)
    organization_name = Column(String, unique=True, index=True)
    db_url = Column(String)
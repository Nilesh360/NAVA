from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.common.security import verify_password, create_access_token
from src.api.database.dynamic_db_handler import get_dynamic_session
from src.api.models.dynamic import AdminUser


router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db: Session = get_dynamic_session(form_data.username)
    user = db.query(AdminUser).filter(AdminUser.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token(user.email)
    return {"access_token": token, "token_type": "bearer"}
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.auth import authenticate_admin, security
from app.database import SessionLocal
from app.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/dashboard")
def get_admin_dashboard(arg_credentials: Depends(security), arg_db: Session = Depends(get_db)):
    if not authenticate_admin(arg_credentials, arg_db):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"message": "Welcome to the Admin Dashboard"}
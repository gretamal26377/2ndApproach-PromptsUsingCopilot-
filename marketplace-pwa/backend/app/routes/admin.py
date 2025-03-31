from fastapi import APIRouter, Depends
from app.utils.auth import authenticate_admin, security

router = APIRouter()

@router.get("/dashboard")
def get_admin_dashboard(credentials: Depends(security)):
    authenticate_admin(credentials)
    return {"message": "Welcome to the Admin Dashboard"}
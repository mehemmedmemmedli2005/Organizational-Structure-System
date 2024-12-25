from fastapi import APIRouter, HTTPException
from app.schemas.manager import ManagerCreate, ManagerResponse
from app.services.manager_service import ManagerService

router = APIRouter()
manager_service = ManagerService()

@router.post("/managers/", response_model=ManagerResponse)
def create_manager(manager: ManagerCreate):
    return manager_service.create_manager(manager)

@router.get("/managers/", response_model=list[ManagerResponse])
def read_managers():
    return manager_service.get_managers()
from fastapi import APIRouter, HTTPException
from app.schemas.department import DepartmentCreate, DepartmentResponse
from app.services.department_service import DepartmentService

router = APIRouter()
department_service = DepartmentService()

@router.post("/departments/", response_model=DepartmentResponse)
def create_department(department: DepartmentCreate):
    return department_service.create_department(department)

@router.get("/departments/", response_model=list[DepartmentResponse])
def read_departments():
    return department_service.get_departments()
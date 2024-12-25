from fastapi import APIRouter, HTTPException
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from app.services.employee_service import EmployeeService

router = APIRouter()
employee_service = EmployeeService()

@router.post("/employees/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate):
    return employee_service.create_employee(employee)

@router.get("/employees/", response_model=list[EmployeeResponse])
def read_employees():
    return employee_service.get_employees()
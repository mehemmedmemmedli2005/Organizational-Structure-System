from typing import List
from app.models.department import Department
from app.schemas.department import DepartmentCreate

class DepartmentService:
    def __init__(self):
        self.departments = []

    def create_department(self, department_data: DepartmentCreate) -> Department:
        department = Department(id=len(self.departments) + 1, **department_data.dict())
        self.departments.append(department)
        return department

    def get_departments(self) -> List[Department]:
        return self.departments
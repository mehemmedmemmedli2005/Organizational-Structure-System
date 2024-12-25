from typing import List
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate

class EmployeeService:
    def __init__(self):
        self.employees = []

    def create_employee(self, employee_data: EmployeeCreate) -> Employee:
        employee = Employee(id=len(self.employees) + 1, **employee_data.dict())
        self.employees.append(employee)
        return employee

    def get_employees(self) -> List[Employee]:
        return self.employees
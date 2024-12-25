from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    department_id: int
    manager_id: int
from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    department_id: int
    manager_id: int

class EmployeeResponse(BaseModel):
    id: int
    name: str
    department_id: int
    manager_id: int

    class Config:
        orm_mode = True
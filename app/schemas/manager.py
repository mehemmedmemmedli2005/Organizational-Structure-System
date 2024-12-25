from pydantic import BaseModel

class ManagerCreate(BaseModel):
    name: str

class ManagerResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
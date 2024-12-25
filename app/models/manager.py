from pydantic import BaseModel

class Manager(BaseModel):
    id: int
    name: str
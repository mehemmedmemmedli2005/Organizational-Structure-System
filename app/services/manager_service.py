from typing import List
from app.models.manager import Manager
from app.schemas.manager import ManagerCreate

class ManagerService:
    def __init__(self):
        self.managers = []

    def create_manager(self, manager_data: ManagerCreate) -> Manager:
        manager = Manager(id=len(self.managers) + 1, **manager_data.dict())
        self.managers.append(manager)
        return manager

    def get_managers(self) -> List[Manager]:
        return self.managers
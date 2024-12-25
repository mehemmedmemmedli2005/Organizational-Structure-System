from fastapi import FastAPI
from app.routes import employee_routes, department_routes, manager_routes

app = FastAPI()

app.include_router(employee_routes.router)
app.include_router(department_routes.router)
app.include_router(manager_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Organizational Structure API"}
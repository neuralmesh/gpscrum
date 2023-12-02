# src/main.py

from fastapi import FastAPI
from .employee import Employee

app = FastAPI()

# Load employee config and create an Employee instance
employee = Employee.load_config("docs/employee/config.yml")

@app.get("/")
def read_root():
    return {"message": str(employee)}


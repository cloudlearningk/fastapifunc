from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Operation(BaseModel):
    num1: float
    num2: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Calculator!"}

@app.post("/add")
def add(op: Operation):
    return {"result": op.num1 + op.num2}

@app.post("/subtract")
def subtract(op: Operation):
    return {"result": op.num1 - op.num2}

@app.post("/multiply")
def multiply(op: Operation):
    return {"result": op.num1 * op.num2}

@app.post("/divide")
def divide(op: Operation):
    if op.num2 == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"result": op.num1 / op.num2}

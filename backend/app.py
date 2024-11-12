from fastapi import FastAPI
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for all origins (use specific origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods, including OPTIONS
    allow_headers=["*"],  # Allows all headers
)


# Define the Math class
class Math:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

    def substract(self):
        return self.a - self.b
# Define request body model
class MathRequest(BaseModel):
    num1: float
    num2: float
    operation: str

@app.post("/math")
def perform_math_operation(request: MathRequest):
    math_operations = Math(request.num1, request.num2)
    
    if request.operation == 'add':
        result = math_operations.add()
    elif request.operation == 'multiply':
        result = math_operations.multiply()
    elif request.operation == 'substract':
        result = math_operations.substract()
    else:
        return {"error": "Invalid operation. Please select 'add', 'multiply' or 'substract'."}

    return {"result": result}



from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional
import uvicorn


app = FastAPI()


students = {
    1 :{
    "name" : "Budi",
    "age" : "17",
    "class" : "B"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

@app.get("/chat")
def main():
    return {"test" : "nah"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0, lt=2)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name:Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in student:
        return {"Error" : "Student exists"}
    students[student_id] = student
    return students[student_id]

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
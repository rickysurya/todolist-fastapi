from typing import Optional

from pydantic import BaseModel, Field


class StudentSchema(BaseModel):
    title: str = Field(...)
    task_description: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "title": "Finish Coursework",
                "task_description": "Chapter 2 of Google Data Analytics Course needs to be finished today",
            }
        }


class UpdateStudentModel(BaseModel):
    title: Optional[str]
    task_description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Finish Coursework",
                "task_description": "Chapter 2 of Google Data Analytics Course needs to be finished today",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
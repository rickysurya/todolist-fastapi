from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional
import uvicorn
from fastapi.params import Body


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/get_tasks")
def get_posts():
    return {
        "Message": "Tasks are retrieved"
    }


@app.post("/create_tasks")
def create_posts(post: dict = Body(...)):
    print(post)
    return {
        "Message": "Tasks are added!"
    }


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")

from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional
import uvicorn
from fastapi.params import Body


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/getposts")
def get_posts():
    return {
        "Message": "Post retrieved successfully"
    }


@app.post("/createposts")
def create_posts(post: dict = Body(...)):
    print(post)
    return {
        "Message": "Post successfully created!"
    }


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")

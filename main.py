from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {'data' : 'blog list'}

@app.get("/blog/published")
def fetchBlog():
    return{"data" : "published"}


@app.get("/blog/{id}")
def fetchBlog(id: int):
    return{"data" : id}



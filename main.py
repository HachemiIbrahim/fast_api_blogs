from typing import Union,Optional
from pydantic import  BaseModel
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {'data' : 'blog list'}

@app.get("/blog")
def fetchBlog(limit = 10 , published : bool = True,sort : Optional[str] = None):
    if(published):
        return {"data" : f"{limit} published blogs"}
    else:
        return {"data" : f"{limit} unplished blogs"}



@app.get("/blog/{id}")
def fetchBlog(id: int , limit=10):
    return{"data" : f"{id} , {limit}"}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]


@app.post("/blog")
def postBlog(request : Blog):
    return {"data": f"this blog is {request.title} and {request.body}"}





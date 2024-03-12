from fastapi import FastAPI
from . import schema

app = FastAPI()

@app.post("/blog")
def creating(request:schema.Blog):
    return request
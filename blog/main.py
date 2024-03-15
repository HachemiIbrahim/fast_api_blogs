from fastapi import FastAPI
from . import schema , models
from .database import Base , engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/blog")
def creating(request:schema.Blog):
    return request
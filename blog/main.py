from fastapi import FastAPI 
from . import models
from .database import Base , engine 
from .routers import user , blog , authentification

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(blog.router)
app.include_router(authentification.router)

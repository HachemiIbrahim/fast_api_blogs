from fastapi import FastAPI , Depends , status , HTTPException , Response
from sqlalchemy.orm import Session
from . import schema , models
from .database import Base , engine , SessionLocal
from .hasing import Hash
from typing import List
from .routers import user , blog

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(blog.router)


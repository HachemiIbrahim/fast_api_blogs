from fastapi import FastAPI , Depends
from sqlalchemy.orm import Session
from . import schema , models
from .database import Base , engine , SessionLocal

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog")
def creating(request:schema.Blog , db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title ,body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
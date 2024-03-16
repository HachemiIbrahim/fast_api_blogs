from fastapi import FastAPI , Depends , status , HTTPException , Response
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

@app.post("/blog" , status_code=status.HTTP_201_CREATED)
def creating(request:schema.Blog , db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title ,body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog")
def show_all( db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.delete("/blog/{id}" , status_code=status.HTTP_200_OK)
def delete(id ,  response : Response,db : Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete()
    db.commit()

@app.get("/blogs/{id}" , status_code=status.HTTP_200_OK)
def get(id ,  response : Response,db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the blog with the id {id} is not found")
    return blog
from fastapi import FastAPI , Depends , status , HTTPException , Response
from sqlalchemy.orm import Session
from . import schema , models
from .database import Base , engine , SessionLocal
from typing import List

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

@app.get("/blog" , response_model=List[schema.ShowBlog])
def show_all( db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.delete("/blog/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete(id ,  response : Response,db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the blog with the id {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    
    
@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schema.Blog,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'detail with id {id} not found')
    blog.update(request.dict())
    db.commit()
    return {'updated'}

@app.get("/blogs/{id}" , status_code=status.HTTP_200_OK , response_model=schema.ShowBlog)
def get(id ,  response : Response,db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the blog with the id {id} is not found")
    return blog


@app.post("/user" , status_code=status.HTTP_201_CREATED)
def create_user(request:schema.User , db : Session = Depends(get_db)):
    user_data = request.dict()
    new_user = models.User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
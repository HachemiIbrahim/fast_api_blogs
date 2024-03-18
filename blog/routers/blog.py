from fastapi import FastAPI , Depends , status , HTTPException , Response , APIRouter
from sqlalchemy.orm import Session
from .. import schema , models
from ..database import Base , engine , SessionLocal , get_db
from ..hasing import Hash
from typing import List


router = APIRouter()

@router.post("/blog" , status_code=status.HTTP_201_CREATED , tags=["blogs"])
def creating(request:schema.Blog , db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title ,body = request.body , user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("/blog" , response_model=List[schema.ShowBlog], tags=["blogs"])
def show_all( db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.delete("/blog/{id}" , status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
def delete(id ,  response : Response,db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the blog with the id {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    
    
@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED ,  tags=["blogs"])
def update(id,request:schema.Blog,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'detail with id {id} not found')
    blog.update(request.dict())
    db.commit()
    return {'updated'}

@router.get("/blogs/{id}" , status_code=status.HTTP_200_OK , response_model=schema.ShowBlog ,  tags=["blogs"])
def get(id ,  response : Response,db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the blog with the id {id} is not found")
    return blog



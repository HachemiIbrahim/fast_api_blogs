from fastapi import FastAPI , Depends , status , HTTPException , Response , APIRouter
from sqlalchemy.orm import Session
from .. import schema , models
from ..database import Base , engine , SessionLocal , get_db
from ..hasing import Hash
from typing import List


router = APIRouter(
 tags=["Blogs"],
 prefix="/blog"
 )

@router.post("/" , status_code=status.HTTP_201_CREATED)
def creating(request:schema.Blog , db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title ,body = request.body , user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("/" , response_model=List[schema.ShowBlog])
def show_all( db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.delete("/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete(id ,  response : Response,db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the blog with the id {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    
    
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED )
def update(id,request:schema.Blog,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'detail with id {id} not found')
    blog.update(request.dict())
    db.commit()
    return {'updated'}

@router.get("/{id}" , status_code=status.HTTP_200_OK , response_model=schema.ShowBlog)
def get(id ,  response : Response,db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the blog with the id {id} is not found")
    return blog



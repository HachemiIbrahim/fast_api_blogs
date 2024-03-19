from sqlalchemy.orm import Session
from .. import models, schema
from fastapi import HTTPException,status

def create(request:schema.Blog , db : Session):
    new_blog = models.Blog(title = request.title ,body = request.body , user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_all( db : Session):
    blogs = db.query(models.Blog).all()
    return blogs

def delete(id :int, db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the blog with the id {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    

def update(id :int ,request:schema.Blog , db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'detail with id {id} not found')
    blog.update(request.dict())
    db.commit()
    return {'updated'}

def get(id:int , db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the blog with the id {id} is not found")
    return blog
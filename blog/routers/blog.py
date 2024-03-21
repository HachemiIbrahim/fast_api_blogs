from fastapi import FastAPI , Depends , status , HTTPException , Response , APIRouter
from sqlalchemy.orm import Session
from .. import schema , models , oauth2
from ..database import Base , engine , SessionLocal , get_db
from ..hasing import Hash
from typing import List
from ..repository import blog

router = APIRouter(
 tags=["Blogs"],
 prefix="/blog"
 )

@router.post("/" , status_code=status.HTTP_201_CREATED)
def creating(request:schema.Blog , db : Session = Depends(get_db),current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.create(request,db)

@router.get("/" , response_model=List[schema.ShowBlog])
def get_all(db:Session = Depends(get_db),current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.delete("/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int ,  response : Response,db : Session = Depends(get_db),current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)
    
    
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED )
def update(id: int,request:schema.Blog,db:Session=Depends(get_db),current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

@router.get("/{id}" , status_code=status.HTTP_200_OK , response_model=schema.ShowBlog)
def get(id:int ,  response : Response,db : Session = Depends(get_db),current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.get(id , db)



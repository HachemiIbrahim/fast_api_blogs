from fastapi import FastAPI , Depends , status , HTTPException , Response , APIRouter
from sqlalchemy.orm import Session
from .. import schema , models
from ..database import Base , engine , SessionLocal , get_db
from ..hasing import Hash
from typing import List
from ..repository import user


router = APIRouter(
     tags=["Users"],
     prefix="/user"
)


@router.post("/" , status_code=status.HTTP_201_CREATED)
def create_user(request:schema.User , db : Session = Depends(get_db)):
    return user.create(request ,db)

@router.get("/{id}" , status_code=status.HTTP_200_OK , response_model=schema.SHowUser)
def get(id:int ,  response : Response,db : Session = Depends(get_db)):
   return user.show(id,db)
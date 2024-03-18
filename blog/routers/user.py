from fastapi import FastAPI , Depends , status , HTTPException , Response , APIRouter
from sqlalchemy.orm import Session
from .. import schema , models
from ..database import Base , engine , SessionLocal , get_db
from ..hasing import Hash
from typing import List


router = APIRouter()


@router.post("/user" , status_code=status.HTTP_201_CREATED ,  tags=["users"])
def create_user(request:schema.User , db : Session = Depends(get_db)):
    new_user = models.User(name=request.name ,email=request.email,password=Hash.bycrypt(request.password) )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/user/{id}" , status_code=status.HTTP_200_OK , response_model=schema.SHowUser ,  tags=["users"])
def get(id ,  response : Response,db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the user with the id {id} is not found")
    return user
from typing import List, Optional
from pydantic import BaseModel

class BlogBase(BaseModel):
    title:str
    body:str
    
class Blog(BlogBase):
    class Config:
        orm_mode = True
    
    
class UserBase(BaseModel):
    name:str
    email:str
    password:str
    
class User(UserBase):    
    class Config:
        orm_mode = True

class SHowUser(BaseModel):
    name:str
    email:str
    blogs : List[Blog] =[]
    class Config:
        orm_mode = True
    
    
class ShowBlog(BaseModel):
    title:str
    body:str
    writenBy:User
    class Config:
        orm_mode = True
        
class login(BaseModel):
    username: str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
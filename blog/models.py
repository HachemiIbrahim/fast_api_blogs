from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer , ForeignKey("users.id"))
    
    writenBy = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="writenBy")


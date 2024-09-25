from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, Integer

class UserBase(BaseModel):
    username: str
    password: str
    user_email: str

class UserDisplay(BaseModel):
    username: str
    user_email: str
    class Config(): 
        orm_mode = True

class PostBase(BaseModel):
  caption: str
  user_id: int
  mediasourcs: str



#Post Display 

class User(BaseModel):
    username: str
    class Config(): 
        orm_mode = True

class PostDisplay(BaseModel):
    post_id: int
    caption: str
    mediasourcs: str
    timestamp: datetime
    user: User
    class Config(): 
        orm_mode = True
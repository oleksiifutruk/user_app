from typing import Optional
from datetime import date
from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    city: Optional[str] = None
    birth_day: Optional[date] = None
    premium: Optional[bool] = False
    ip: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

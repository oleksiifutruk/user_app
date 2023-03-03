from sqlalchemy import Column, Integer, String, Date, Boolean
from .database import Base



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    gender = Column(String(12))
    age = Column(Integer)
    city = Column(String(50))
    birth_day = Column(Date)
    premium = Column(Boolean)
    ip = Column(String(50))

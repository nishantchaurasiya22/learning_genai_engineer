from  sqlalchemy import Column,Integer,String
from src.config.db import Base

class UserModel(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    user_name=Column(String(100),unique=True,nullable=False)
    email=Column(String(250),unique=True,nullable=False)
    password=Column(String(250),nullable=False)


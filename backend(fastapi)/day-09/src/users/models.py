from src.config.db import base
from sqlalchemy import Column,Integer,String

class UserModel(base):
    __tablename__="Users_table"
    id=Column(Integer,primary_key=True)
    user_name=Column(String(150),unique=True,nullable=False)
    email=Column(String(250),unique=True,nullable=False)
    password=Column(String(250),nullable=False)

    
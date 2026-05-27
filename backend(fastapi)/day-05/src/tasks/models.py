from sqlalchemy import Column,Integer,String,Boolean
from src.config.db import base
class TaskModel(base):
    __tablename__="user_tasks"

    id=Column(Integer,primary_key=True)
    title=Column(String(100),nullable=False)
    description=Column(String(250),nullable=False)
    is_completed=Column(Boolean,default=False)


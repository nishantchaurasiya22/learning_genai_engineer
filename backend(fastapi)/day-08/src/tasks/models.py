from src.config.db import base
from sqlalchemy import Column,String,Integer,Boolean

class TaskModel(base):
    __tablename__="tasks_table"
    id=Column(Integer,primary_key=True)
    title=Column(String(150),nullable=False)
    description=Column(String(250),nullable=False)
    is_completed=Column(Boolean,default=False)
    
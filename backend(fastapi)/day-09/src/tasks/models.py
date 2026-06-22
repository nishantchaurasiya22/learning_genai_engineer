from src.config.db import base
from sqlalchemy import Column,Integer,String,Boolean

class TaskModel(base):
    __tablename__="task_table"
    id=Column(Integer,primary_key=True)
    title=Column(String(150),nullable=False)
    description=Column(String(250),nullable=False)
    is_completed=Column(Boolean,default=False)

    
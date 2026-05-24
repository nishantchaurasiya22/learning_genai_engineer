from sqlalchemy import Column,Integer,String,Boolean
from src.config.db import base
class TaskModel(base):
    __tablename__="task_user"

    id=Column(Integer,primary_key=True)
    title=Column(String(100),nullable=False)
    description=Column(String(500),nullable=False)
    is_completed=Column(Boolean,default=False)

    
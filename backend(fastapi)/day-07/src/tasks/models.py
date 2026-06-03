from sqlalchemy import Column,String,Integer,Boolean,ForeignKey
from src.config.db import base
class TaskModel(base):
    __tablename__="tasks"
    id=Column(Integer,primary_key=True)
    title=Column(String(150),nullable=False)
    description=Column(String(250),nullable=False)
    is_completed=Column(Boolean,default=False)
    
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"))
    
    
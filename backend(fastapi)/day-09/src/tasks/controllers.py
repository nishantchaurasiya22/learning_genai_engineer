from src.tasks.models import TaskModel
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from src.users.models import UserModel
from src.tasks.dtos import TaskSchema,UpdateTaskSchema
def create(body:TaskSchema,db:Session,user:UserModel):
    data=body.model_dump()
    new_task=TaskModel(
        title=data["title"],
        description=data["description"],
        user_id=user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db:Session):
    tasks=db.query(TaskModel).all()
    return tasks

def get_task(task_id:int,db:Session):
    task=db.query(TaskModel).filter(TaskModel.id==task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    return task

def update_task(task_id:int,body:UpdateTaskSchema,db:Session):
    task=db.query(TaskModel).filter(TaskModel.id==task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    for field,value in body.model_dump().items():
        setattr(task,field,value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(task_id:int,db:Session):
    task=db.query(TaskModel).filter(TaskModel.id==task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    db.delete(task)
    db.commit()
    return None
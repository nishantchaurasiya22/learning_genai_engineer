from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from src.users.models import UserModel
from src.tasks.dtos import TaskSchema,UpdateTaskSchema
from fastapi import HTTPException,status
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

def get_tasks(db:Session,user:UserModel):
    tasks=db.query(TaskModel).filter(TaskModel.user_id==user.id).all()
    if not tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="You have not created any task ")
    return tasks

def get_task(task_id:int,db:Session,user:UserModel):
    task=db.query(TaskModel).filter(
        TaskModel.id==task_id,
        TaskModel.user_id==user.id 
    ).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    return task

def update_task(task_id:int,body:UpdateTaskSchema,db:Session,user:UserModel):
    task=db.query(TaskModel).filter(
        TaskModel.id==task_id,
        TaskModel.user_id==user.id
    ).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    for field,value in body.model_dump().items():
        setattr(task,field,value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(task_id:int,db:Session,user:UserModel):
    task=db.query(TaskModel).filter(
        TaskModel.id==task_id,
        TaskModel.user_id==user.id
    ).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    db.delete(task)
    db.commit()
    return None
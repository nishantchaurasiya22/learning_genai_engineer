from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.tasks.models import TaskModel
def create_task(body:TaskSchema,db:Session):
    data=body.model_dump()
    new_data=TaskModel(
        title=data["title"],
        description=data["description"]
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

def get_tasks(db:Session):
    all_tasks=db.query(TaskModel).all()
    return all_tasks

def get_task(task_id:int,db:Session):
    task=db.query(TaskModel).filter(TaskModel.id==task_id).first()
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return task

def update_task(task_id:int,body:TaskSchema,db:Session):
    task=db.query(TaskModel).filter(TaskModel.id==task_id).first()
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    for field,value in body.model_dump().items():
        setattr(task,field,value)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def delete_task(task_id:int,db:Session):
    task=db.query(TaskModel).filter(TaskModel.id==task_id).first()
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    db.delete(task)
    db.commit()
    return None
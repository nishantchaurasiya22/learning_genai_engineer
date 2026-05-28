from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from src.tasks.models import TaskModel
def create_task(body:TaskSchema,db:Session):
    data=body.model_dump()
    new_task=TaskModel(
        title=data["title"],
        description=data["description"]
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db:Session):
    all_tasks=db.query(TaskModel).all()
    return all_tasks

def get_task(task_id:int,db:Session):
    task=db.query(TaskModel).filter(TaskModel.id==task_id).first()
    if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return task
    
def update_task(task_id:int,body:TaskSchema,db:Session):
    task=db.query(TaskModel).filter(TaskModel.id==task_id).first()
    if not task:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    for field,value in body.model_dump().items():
        setattr(task,field,value)
    db.commit()
    db.refresh(task)
    return task
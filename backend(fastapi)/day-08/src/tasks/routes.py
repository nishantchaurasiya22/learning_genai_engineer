from fastapi import APIRouter,status,Depends
from src.tasks.dtos import TaskSchema,ResponseTaskSchema,UpdateTaskSchema
from sqlalchemy.orm import Session
from typing import List
from src.tasks import controllers
from src.config.db import get_db
task_auth=APIRouter(prefix="/tasks")

@task_auth.post("/create",response_model=ResponseTaskSchema,status_code=status.HTTP_201_CREATED)
def create(body:TaskSchema,db:Session=Depends(get_db)):
    return controllers.create(body,db)

@task_auth.get("/get_tasks",response_model=List[ResponseTaskSchema],status_code=status.HTTP_200_OK)
def get_tasks(db:Session=Depends(get_db)):
    return controllers.get_tasks(db)

@task_auth.get("/get_task/{task_id}",response_model=ResponseTaskSchema,status_code=status.HTTP_200_OK)
def get_task(task_id:int,db:Session=Depends(get_db)):
    return controllers.get_task(task_id,db)

@task_auth.put("/update_task/{task_id}",response_model=ResponseTaskSchema,status_code=status.HTTP_200_OK)
def update_task(task_id:int,body:UpdateTaskSchema,db:Session=Depends(get_db)):
    return controllers.update_task(task_id,body,db)

@task_auth.delete("/delete_task/{task_id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db:Session=Depends(get_db)):
    return controllers.delete_task(task_id,db)
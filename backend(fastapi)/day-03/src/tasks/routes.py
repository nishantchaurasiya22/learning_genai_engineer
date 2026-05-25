from fastapi import APIRouter,Depends,status
from typing import List
from src.tasks.dtos import TaskSchema,TaskResponseSchema
from src.config.db import get_db
from sqlalchemy.orm import Session
from src.tasks import controllers
task_route=APIRouter(prefix="/tasks")

@task_route.post("/create",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema,db:Session=Depends(get_db)):
    return controllers.create_task(body,db)


@task_route.get("/get_tasks",response_model=List[TaskResponseSchema],status_code=status.HTTP_200_OK)
def create_task(db:Session=Depends(get_db)):
    return controllers.get_tasks(db)

@task_route.get("/get_task/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_200_OK)
def get_task(task_id:int,db:Session=Depends(get_db)):
    return controllers.get_task(task_id,db)

@task_route.put("/update_task/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_200_OK)
def update_task(task_id:int,body:TaskSchema,db:Session=Depends(get_db)):
    return controllers.update_task(task_id,body,db)

@task_route.delete("/delete_task/{task_id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db:Session=Depends(get_db)):
    return controllers.delete_task(task_id,db)
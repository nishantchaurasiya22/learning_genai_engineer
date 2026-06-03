from fastapi import APIRouter,status,Depends
from src.tasks.dtos import TaskSchema,TaskResponseSchema,TaskUpdateSchema
from src.tasks import controllers
from typing import List
from src.utils.helper import is_auth
from src.users.models import UserModel
from src.config.db import get_db
from sqlalchemy.orm import Session
task_routes=APIRouter(prefix="/tasks")

@task_routes.post("/create",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_auth)):
    return controllers.create_task(body,db)

@task_routes.get("/get_tasks",response_model=List[TaskSchema],status_code=status.HTTP_200_OK)
def get_tasks(db:Session=Depends(get_db),user:UserModel=Depends(is_auth)):
    return controllers.get_tasks(db)

@task_routes.get("/get_task/{task_id}",response_model=TaskSchema,status_code=status.HTTP_200_OK)
def get_task(task_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_auth)):
    return controllers.get_task(task_id,db)

@task_routes.patch("/update_task/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_200_OK)
def update_task(task_id:int,body:TaskUpdateSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_auth)):
    return controllers.update_task(task_id,body,db)

@task_routes.delete("/delete_task/{task_id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_auth)):
    return controllers.delete_task(task_id,db)
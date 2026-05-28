from fastapi import APIRouter,status,Depends
from typing import List
from src.tasks.dtos import TaskSchema,TaskResponseSchema
from sqlalchemy.orm import Session
from src.utils.helpers import is_auth
from src.tasks import controllers
from src.config.db import get_db
from src.users.model import UserModel
task_routes=APIRouter(prefix="/tasks")

@task_routes.post("/create",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def create(body:TaskSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_auth)):
    return controllers.create_task(body,db)

@task_routes.get("/get_tasks",response_model=List[TaskResponseSchema],status_code=status.HTTP_200_OK)
def all_tasks(db:Session=Depends(get_db),user:UserModel=Depends(is_auth)):
    return controllers.get_tasks(db)

@task_routes.get("/get_task/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_200_OK)
def task(task_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_auth)):
    return controllers.get_task(task_id,db)

@task_routes.put("/update_task/{task_id}",response_model=None,status_code=status.HTTP_200_OK)
def update_task(task_id:int,body:TaskSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_auth)):
    return controllers.update_task(task_id,body,db)

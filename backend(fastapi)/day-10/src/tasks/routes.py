from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from src.tasks import controllers
from typing import List
from src.config.db import get_db
from src.utils.helper import is_auth
from src.users.models import UserModel
from src.tasks.dtos import TaskSchema,ResponseTasKSchema,UpdateTaskSchema
task_route=APIRouter(prefix="/tasks")

@task_route.post("/create",response_model=ResponseTasKSchema,status_code=status.HTTP_201_CREATED)
def create(body:TaskSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_auth)):
    return controllers.create(body,db,user)

@task_route.get("/get_tasks",response_model=List[ResponseTasKSchema],status_code=status.HTTP_200_OK)
def get_tasks(db:Session=Depends(get_db),user:UserModel=Depends(is_auth)):
    return controllers.get_tasks(db,user)

@task_route.get("/get_task/{task_id}",response_model=ResponseTasKSchema,status_code=status.HTTP_200_OK)
def get_task(task_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_auth)):
    return controllers.get_task(task_id,db,user)

@task_route.put("/update_task/{task_id}",response_model=ResponseTasKSchema,status_code=status.HTTP_200_OK)
def update_task(task_id:int,body:UpdateTaskSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_auth)):
    return controllers.update_task(task_id,body,db,user)

@task_route.delete("/delete_task/{task_id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_auth)):
    return controllers.delete_task(task_id,db,user)
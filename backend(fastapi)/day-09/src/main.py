from fastapi import FastAPI
from src.config.db import base,engine
from src.tasks.routes import task_route
from src.users.routes import auth_route
from src.tasks.models import TaskModel
from src.users.models import UserModel
base.metadata.create_all(engine)
app=FastAPI()
app.include_router(task_route)
app.include_router(auth_route)
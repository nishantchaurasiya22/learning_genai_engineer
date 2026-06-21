from fastapi import FastAPI
from src.config.db import engine,base
from src.tasks.models import TaskModel
from src.tasks.routes import task_auth
from src.users.routes import auth_route
from src.users.models import UserModel
base.metadata.create_all(engine)
app=FastAPI()
app.include_router(task_auth)
app.include_router(auth_route)

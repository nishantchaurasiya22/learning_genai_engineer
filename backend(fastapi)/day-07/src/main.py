from fastapi import FastAPI
from src.config.db import base,engine
from src.tasks.models import TaskModel
from src.users.models import UserModel
from src.tasks.routes import task_routes
from src.users.routes import auth_routes
base.metadata.create_all(engine)
app=FastAPI()

@app.get("/")
def root():
    return {
        "message":"hello world"
    }
app.include_router(task_routes)
app.include_router(auth_routes)
from fastapi import FastAPI
from src.config.db import base,engine
from src.tasks.routes import task_routes
from src.tasks.models import TaskModel
from src.users.model import UserModel
from src.users.routes import auth_routes
app=FastAPI()

base.metadata.create_all(engine)
@app.get("/")
def root():
    return({
        "message":"hello from fastapi"
    })

app.include_router(task_routes)
app.include_router(auth_routes)
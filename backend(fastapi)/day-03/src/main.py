from fastapi import FastAPI
from src.config.db import Base,engine
from src.tasks.models import TaskModel
from src.users.models import UserModel
from src.tasks.routes import task_route
from src.users.routes import auth_route
Base.metadata.create_all(engine)
app=FastAPI()
@app.get("/")
def root():
    return{
        "message":"hello from fastapi"
    }

app.include_router(task_route)
app.include_router(auth_route)
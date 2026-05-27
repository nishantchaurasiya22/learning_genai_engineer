from fastapi import FastAPI
from src.config.db import engine,base
from src.tasks.routes import task_routes
from src.users.routes import auth_routes
from src.tasks.models import TaskModel
from src.users.models import UserModel
base.metadata.create_all(engine)
app=FastAPI()
@app.get("/")
def root():
    return {
        "message":"hello from fastapi"
}
app.include_router(task_routes)
app.include_router(auth_routes)
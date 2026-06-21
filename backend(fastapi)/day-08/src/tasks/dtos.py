from pydantic import BaseModel

class TaskSchema(BaseModel):
    title:str
    description:str
    is_completed:bool=False

class ResponseTaskSchema(TaskSchema):
    id:int

class UpdateTaskSchema(BaseModel):
    is_completed:bool

    class Config:
        from_attributes=True


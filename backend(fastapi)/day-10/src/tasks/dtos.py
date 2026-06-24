from pydantic import BaseModel

class TaskSchema(BaseModel):
    title:str
    description:str
    is_completed:bool=False

class ResponseTasKSchema(TaskSchema):
    id:int
    user_id:int

class UpdateTaskSchema(BaseModel):
    is_completed:bool

    class Config:
        from_attributes=True
        
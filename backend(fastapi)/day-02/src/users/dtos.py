from pydantic import BaseModel
class UserSchema(BaseModel):

    user_name:str
    email:str
    password:str
class UserResponseSchema(BaseModel):
    id: int
    user_name: str
    email: str

    class Config:
        from_attributes = True 
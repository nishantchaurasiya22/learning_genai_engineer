from pydantic import BaseModel,EmailStr
class UserSchema(BaseModel):
    user_name:str
    email:EmailStr
    password:str

class ReponseUserSchema(BaseModel):
    id:int
    user_name:str
    email:EmailStr

class LoginUserSchema(BaseModel):
    identifier:str
    password:str

    class Config:
        from_attributes=True
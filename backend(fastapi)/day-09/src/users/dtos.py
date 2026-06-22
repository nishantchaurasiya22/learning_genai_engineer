from pydantic import BaseModel,EmailStr
class UserSchema(BaseModel):
    user_name:str
    email:EmailStr
    password:str

class ResponseUserSchema(BaseModel):
    id:int
    user_name:str
    email:EmailStr

class LoginSchema(BaseModel):
    identifier:str
    password:str

    class Config:
        from_attributes=True

    
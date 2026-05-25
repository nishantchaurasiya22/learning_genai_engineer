from pydantic import BaseModel,EmailStr
class UserSchema(BaseModel):
    user_name:str
    email:EmailStr
    password:str

class UserResponseSchema(BaseModel):
    id:int
    user_name:str
    email:EmailStr
     
    class Config:
         from_attributes=True

class LoginSchema(BaseModel):
    user_name:str
    password:str
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
        from_attribute=True

class LoginSchema(BaseModel):
    identifier:str
    password:str
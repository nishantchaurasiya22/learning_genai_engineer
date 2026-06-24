from pydantic import BaseModel,EmailStr

class UserSchema(BaseModel):
    user_name:str
    email:EmailStr
    password:str

class ReponseUserSchema(BaseModel):
    id:int
    user_name:str
    email:EmailStr

class loginUserSchema(BaseModel):
    identifier:str
    password:str

class ResponseLoginSchema(BaseModel):
    message:str

    
    class Config:
        from_attributes=True

from pydantic import BaseModel,EmailStr

class UserSchema(BaseModel):
    user_name:str
    email:EmailStr
    password:str

class UserReponseSchema(BaseModel):
    id:int
    user_name:str
    email:EmailStr
    
    class Config:
        from_attributes=True


class LoginSchema(BaseModel):
    identifier:str
    password:str


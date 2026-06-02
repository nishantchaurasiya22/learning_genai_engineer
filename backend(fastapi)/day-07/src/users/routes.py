from fastapi import APIRouter,status,Depends
from src.users import controllers
from sqlalchemy.orm import Session
from src.users.dtos import UserSchema,UserResponseSchema,LoginSchema
from src.config.db import get_db
auth_routes=APIRouter(prefix="/auth")

@auth_routes.post("/register",response_model=UserResponseSchema,status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session=Depends(get_db)):
    return controllers.register(body,db)

@auth_routes.post("/login",status_code=status.HTTP_200_OK)
def login(body:LoginSchema,db:Session=Depends(get_db)):
    return controllers.login(body,db)
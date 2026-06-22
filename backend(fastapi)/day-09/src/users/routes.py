from fastapi import APIRouter,Depends,status
from src.users.dtos import UserSchema,ResponseUserSchema,LoginSchema
from sqlalchemy.orm import Session
from src.users import controllers
from src.config.db import get_db
auth_route=APIRouter(prefix="/auth")


@auth_route.post("/register",response_model=ResponseUserSchema,status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session=Depends(get_db)):
    return controllers.register(body,db)

@auth_route.post("/login",status_code=status.HTTP_200_OK)
def login(body:LoginSchema,db:Session=Depends(get_db)):
    return controllers.login(body,db)
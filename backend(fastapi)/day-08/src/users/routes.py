from fastapi import APIRouter,status,Depends,Request
from src.users import controllers
from src.config.db import get_db
from src.users.dtos import UserSchema,ResponseUserSchema,LoginSchema
from sqlalchemy.orm import Session
auth_route=APIRouter(prefix="/auth")

@auth_route.post("/register",response_model=ResponseUserSchema,status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session=Depends(get_db)):
    return controllers.register(body,db)

@auth_route.post("/login",status_code=status.HTTP_200_OK)
def login(body:LoginSchema,db:Session=Depends(get_db)):
    return controllers.login(body,db)

@auth_route.get("/is_auth",response_model=ResponseUserSchema,status_code=status.HTTP_200_OK)
def is_auth(request:Request,db:Session=Depends(get_db)):
    return controllers.is_auth(request,db)
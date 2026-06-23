from fastapi import APIRouter,status,Depends
from src.config.db import get_db
from src.users import controllers
from sqlalchemy.orm import Session
from src.users.dtos import UserSchema,ReponseUserSchema,LoginUserSchema
auth_route=APIRouter(prefix="/auth")

@auth_route.post("/register",response_model=ReponseUserSchema,status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session=Depends(get_db)):
    return controllers.register(body,db)

@auth_route.post("/login",status_code=status.HTTP_200_OK)
def login(body:LoginUserSchema,db:Session=Depends(get_db)):
    return controllers.login(body,db)
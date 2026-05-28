from fastapi import APIRouter,status,Depends,Request
from src.users import controllers
from sqlalchemy.orm import Session
from src.config.db import get_db

from src.users.dtos import UserSchema,UserResponseSchema,LoginSchema
auth_routes=APIRouter(prefix="/auth")

@auth_routes.post("/register",response_model=UserResponseSchema,status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session=Depends(get_db)):
    return controllers.register(body,db)


@auth_routes.get("/is_auth",response_model=UserResponseSchema,status_code=status.HTTP_200_OK)
def is_auth(request:Request,db:Session=Depends(get_db)):
    return controllers.is_auth(request,db)


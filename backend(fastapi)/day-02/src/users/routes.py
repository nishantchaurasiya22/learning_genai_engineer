from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.users.dtos import UserSchema,UserResponseSchema
from src.users import controllers
auth_route=APIRouter(prefix="/auth")


@auth_route.post("/register",response_model=UserResponseSchema,status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session=Depends(get_db)):
    return controllers.register(body,db)
from fastapi import APIRouter,Depends,status,Request
from src.users import controllers
from src.users.dtos import UserSchema,UserReponseSchema,LoginSchema
from sqlalchemy.orm import Session
from src.config.db import get_db
auth_routes=APIRouter(prefix="/auth")

@auth_routes.post("/register",response_model=UserReponseSchema,status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session=Depends(get_db)):
    return controllers.register(body,db)

@auth_routes.post("/login",status_code=status.HTTP_200_OK)
def login(body:LoginSchema,db:Session=Depends(get_db)):
    return controllers.login(body,db)

@auth_routes.get("/is_auth",response_model=UserReponseSchema,status_code=status.HTTP_200_OK)
def is_auth(request:Request,db:Session=Depends(get_db)):
    return controllers.is_authenticated(request,db)
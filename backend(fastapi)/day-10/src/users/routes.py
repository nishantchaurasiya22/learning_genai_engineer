from fastapi import APIRouter,status,HTTPException,Depends
from src.users.dtos import UserSchema,ReponseUserSchema,loginUserSchema,ResponseLoginSchema
from sqlalchemy.orm import Session
from src.users import controllers
from fastapi import Response
from src.config.db import get_db
auth_route=APIRouter(prefix="/auth")

@auth_route.post("/register",response_model=ReponseUserSchema,status_code=status.HTTP_201_CREATED)
async def register(body:UserSchema,db:Session=Depends(get_db)):
    return await controllers.register(body,db)

@auth_route.post("/login",response_model=ResponseLoginSchema,status_code=status.HTTP_200_OK)
def login(body:loginUserSchema,response:Response,db:Session=Depends(get_db)):
    return controllers.login(body,response,db)
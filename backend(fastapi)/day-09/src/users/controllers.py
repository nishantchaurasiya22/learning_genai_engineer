from sqlalchemy.orm import Session
import jwt
from src.config.settings import settings
from datetime import datetime,timedelta
from pwdlib import PasswordHash
from src.users.dtos import UserSchema,LoginUserSchema
from fastapi import HTTPException,status
from sqlalchemy import or_
pwd=PasswordHash.recommended()
from src.users.models import UserModel

def register(body:UserSchema,db:Session):
    is_user=db.query(UserModel).filter(
        or_(
            UserModel.user_name==body.user_name,
            UserModel.email==body.email
        )
    ).first()
    if is_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User already exist")
    hash_password=pwd.hash(body.password)
    new_user=UserModel(
        user_name=body.user_name,
        email=body.email,
        password=hash_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login(body:LoginUserSchema,db:Session):
    user=db.query(UserModel).filter(
       or_(
           UserModel.user_name==body.identifier,
           UserModel.email==body.identifier
       )
    ).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    is_valid=pwd.verify(body.password,user.password)
    if not is_valid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid password")
    EXP_TIME=datetime.now()+timedelta(minutes=settings.EXP_TIME)
    token=jwt.encode({"_id":user.id,"exp":EXP_TIME},settings.SECRET_KEY,settings.ALGORITHM)
    return{
        "token":token
    }
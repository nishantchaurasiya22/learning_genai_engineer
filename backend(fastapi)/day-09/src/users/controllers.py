from src.users.dtos import UserSchema,LoginSchema
from pwdlib import PasswordHash
import jwt
from datetime import datetime,timedelta
from src.config.settings import settings
from fastapi import HTTPException,status
from src.users.models import UserModel
from sqlalchemy import or_
pwd=PasswordHash.recommended()
from sqlalchemy.orm import Session

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

def login(body:LoginSchema,db:Session):
    user=db.query(UserModel).filter(
        or_(
            UserModel.email==body.identifier,
            UserModel.user_name==body.identifier
        )
    ).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    is_valid=pwd.verify(body.password,user.password)
    if not is_valid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid password")
    EXP_TIME=datetime.now()+timedelta(minutes=settings.EXP_TIME)
    token=jwt.encode({"_id":user.id,"exp":EXP_TIME},settings.SECRET_KEY,settings.ALGORITHM)
    return {
        "token":token
    }

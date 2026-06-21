from sqlalchemy.orm import Session
from src.users.dtos import UserSchema,LoginSchema
from pwdlib import PasswordHash
from src.users.models import UserModel
from fastapi import HTTPException,status,Request
import jwt
from jwt.exceptions import InvalidTokenError
from src.config.settings import settings
from datetime import datetime,timedelta
from sqlalchemy import or_
pwd=PasswordHash.recommended()
def register(body:UserSchema,db:Session):
    is_user=db.query(UserModel).filter(
        or_(
           UserModel.user_name==body.user_name,
           UserModel.email==body.email
        )
    ).first()
    if is_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="user already exist")
    
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
        UserModel.user_name==body.identifier,
        UserModel.email==body.identifier
        )
    ).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    is_valid=pwd.verify(body.password,user.password)
    if not is_valid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid password")
    exp_time=datetime.now()+timedelta(minutes=settings.EXP_TIME)
    token=jwt.encode({"_id":user.id,"exp":exp_time},settings.SECRET_KEY,settings.ALGORITHM)
    return {
        "token":token
    }


def is_auth(request:Request,db:Session):
    try:
        token=request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Aunthorized User")
        data=jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)
        user_id=data.get("_id")
        user=db.query(UserModel).filter(UserModel.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Aunthorized User")
        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Aunthorized User")
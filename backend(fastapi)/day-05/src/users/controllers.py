from src.users.dtos import UserSchema,LoginSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException,status,Request
from src.users.models import UserModel
from sqlalchemy import or_
from datetime import datetime,timedelta
from src.config.settings import settings
from pwdlib import PasswordHash
import jwt
from jwt.exceptions import InvalidTokenError 
password_hash = PasswordHash.recommended()

def register(body:UserSchema,db:Session):
    is_user=db.query(UserModel).filter(UserModel.user_name==body.user_name).first()
    if is_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User already exist")
    is_user=db.query(UserModel).filter(UserModel.email==body.email).first()
    if is_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User already exist")
    hash_password=password_hash.hash(body.password)
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
    is_user=db.query(UserModel).filter(
          or_(
        UserModel.user_name == body.identifier,
        UserModel.email == body.identifier)).first()
    if not is_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    is_valid=password_hash.verify(body.password,is_user.password)
    if not is_valid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid password")
    exp_time=datetime.now()+timedelta(seconds=2)
    token=jwt.encode({"_id":is_user.id,"exp":exp_time},settings.SECRET_KEY,settings.ALGORITHM)
    return{
        "token":token
    }


def is_authenticated(request:Request,db:Session):
    try:
        token=request.headers.get("authorized")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unathorized User")
        token=token.split(" ")[-1]
        data=jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)
        user_id=data.get("_id")
        user=db.query(UserModel).filter(UserModel.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unathorized User")

    
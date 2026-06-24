from src.users.dtos import UserSchema,loginUserSchema
from sqlalchemy.orm import Session
from fastapi import Response
from pwdlib import PasswordHash
from src.config.settings import settings
from datetime import datetime,timedelta
pwd=PasswordHash.recommended()
import jwt
from fastapi import HTTPException,status
from src.users.models import UserModel
from sqlalchemy import or_
from src.services.mail import send_email

async def register(body:UserSchema,db:Session):
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
    res=await send_email([new_user.email])
    print(res)
    return new_user
    
def login(body:loginUserSchema,response:Response,db:Session):
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
    token=jwt.encode({"_id":user.id,"exp":EXP_TIME},settings.SECRET_KEY,algorithm=settings.ALGORITHM)
    response.set_cookie(
        key="token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=settings.EXP_TIME*60
    )
    return{
        "message":"Login successfully"
    }


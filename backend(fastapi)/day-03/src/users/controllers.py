from src.users.dtos import UserSchema,LoginSchema
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from src.users.models import UserModel
from fastapi import HTTPException,status
import jwt
password_hash = PasswordHash.recommended()
def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def register(body:UserSchema,db:Session):
    is_user=db.query(UserModel).filter(body.user_name==UserModel.user_name).first()
    if is_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User already exist")
    is_user=db.query(UserModel).filter(body.email==UserModel.email).first()
    if is_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User already exist")
    
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
    user=db.query(UserModel).filter(body.user_name==UserModel.user_name).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid email")
    if not verify_password(body.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid password") 
    return{
        "message":"login successfully",
        "data":body
    }
     
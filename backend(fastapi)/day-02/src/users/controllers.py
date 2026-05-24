from src.users.dtos import UserSchema
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.users.models import UserModel
from pwdlib import PasswordHash
password_hash = PasswordHash.recommended()
def get_password_hash(password):
    return password_hash.hash(password)

def register(body:UserSchema,db:Session):
    is_user=db.query(UserModel).filter(UserModel.user_name==body.user_name).first()
    if is_user:
        raise HTTPException(status_code=400,detail="User already exist")
    is_user=db.query(UserModel).filter(UserModel.email==body.email).first()
    if is_user:
        raise HTTPException(status_code=400,detail="User already exist")
    hash_password=get_password_hash(body.password)
    new_user=UserModel(
        user_name=body.user_name,
        email=body.email,
        password=hash_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
   
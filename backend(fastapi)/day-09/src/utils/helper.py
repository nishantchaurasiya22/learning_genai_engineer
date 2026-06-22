from fastapi import Request,Depends,HTTPException,status
import jwt
from jwt.exceptions import InvalidTokenError
from src.config.settings import settings
from src.users.models import UserModel
from src.config.db import get_db
from sqlalchemy.orm import Session
def is_auth(request:Request,db:Session=Depends(get_db)):
    try:
        token=request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized user")
        data=jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)
        user_id=data.get("_id")
        user=db.query(UserModel).filter(UserModel.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized user")
        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized user")

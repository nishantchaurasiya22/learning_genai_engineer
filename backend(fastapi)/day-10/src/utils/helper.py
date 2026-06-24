from sqlalchemy.orm import Session
from src.users.models import UserModel
from jwt.exceptions import InvalidTokenError
from src.config.db import get_db
from src.config.settings import settings
from fastapi import Depends,status,HTTPException,Cookie
import jwt
def is_auth(db:Session=Depends(get_db),token:str=Cookie(None,alias="token")):
    try:
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized User")
        data=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        user_id=data.get("_id")
        user=db.query(UserModel).filter(UserModel.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized User")
        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized User")
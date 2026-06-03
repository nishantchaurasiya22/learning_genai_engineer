from fastapi import Request,status,HTTPException,Depends
from src.config.settings import settings
from src.users.models import UserModel
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session
from src.config.db import get_db
import jwt
def is_auth(request:Request,db:Session=Depends(get_db)):
    try:
        token=request.headers.get("authorized")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Plz login first")
        data=jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)
        user_id=data.get("_id")
        user=db.query(UserModel).filter(UserModel.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized user")
    

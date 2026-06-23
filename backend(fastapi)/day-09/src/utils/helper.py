from fastapi import Request,status,HTTPException,Depends
from src.config.db import get_db
from src.users.models import UserModel
from sqlalchemy.orm import Session
from src.config.settings import settings
from src.config.db import get_db
import jwt
from jwt.exceptions import InvalidTokenError
def is_auth(request:Request,db:Session=Depends(get_db)):
    try:
        token=request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized User")
        data=jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)
        user_id=data.get("_id")
        user=db.query(UserModel).filter(UserModel.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized User")
        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Unauthorized User")

        

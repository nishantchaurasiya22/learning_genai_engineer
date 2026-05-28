from jwt.exceptions import InvalidTokenError
from fastapi import HTTPException,status,Request,Depends
from src.users.model import UserModel
from src.config.db  import get_db
from src.config.settings import settings
import jwt
from sqlalchemy.orm import Session
def is_auth(request:Request,db:Session=Depends(get_db)):
    try:
        token=request.headers.get("authorized")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="authorized user")
        data=jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)
        user_id=data.get("_id")
        user=db.query(UserModel).filter(UserModel.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Authorized User")
 
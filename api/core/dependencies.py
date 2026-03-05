from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from patients.models import User
from api.core.security import SECRET_KEY, ALGORITHM

security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):

    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")

        user = User.objects.get(id=user_id)

        return user

    except (JWTError, User.DoesNotExist):
        raise HTTPException(status_code=401, detail="Invalid token")
    
def require_role(role: str):
    
    def role_checker(user: User = Depends(get_current_user)):

        if user.role != role:
            raise HTTPException(status_code=403, detail="Permission denied")

        return user

    return role_checker
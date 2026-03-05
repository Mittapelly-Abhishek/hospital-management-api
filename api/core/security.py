from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "SUPER_SECRET_KEY"
ALGORITHM = "HS256"


def create_access_token(data: dict):

    expire = datetime.utcnow() + timedelta(hours=2)

    data.update({"exp": expire})

    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
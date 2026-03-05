from fastapi import APIRouter, HTTPException
from patients.models import User
from api.schemas.auth_schema import RegisterRequest, LoginRequest
from api.services.auth_service import hash_password, verify_password
from api.core.security import create_access_token

router = APIRouter()


@router.post("/register")
def register(data: RegisterRequest):

    if User.objects.filter(username=data.username).exists():
        raise HTTPException(status_code=400, detail="User already exists")

    user = User.objects.create(
        username=data.username,
        password=hash_password(data.password),
        role=data.role
    )

    return {"message": "User created"}


@router.post("/login")
def login(data: LoginRequest):

    try:
        user = User.objects.get(username=data.username)
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_access_token({
        "user_id": user.id,
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
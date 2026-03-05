from pydantic import BaseModel
from enum import Enum


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    DOCTOR = "DOCTOR"
    STAFF = "STAFF"


class RegisterRequest(BaseModel):
    username: str
    password: str
    role: UserRole


class LoginRequest(BaseModel):
    username: str
    password: str
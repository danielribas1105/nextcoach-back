from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# Dados para criar um usuário (entrada)
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    senha: str
    image: Optional[str] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    age: Optional[int] = None
    bodyFatPercentage: Optional[float] = None


class UserUpdate(BaseModel):
    name: Optional[str] = None
    image: Optional[str] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    age: Optional[int] = None
    bodyFatPercentage: Optional[float] = None


# Dados retornados ao cliente (saída — nunca expõe a senha)
class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    emailVerified: bool
    image: Optional[str]
    weight: Optional[float]
    height: Optional[float]
    age: Optional[int]
    bodyFatPercentage: Optional[float]
    createdAt: datetime

    class Config:
        from_attributes = True  # Permite converter model SQLAlchemy → Pydantic


# Schema para login
class LoginRequest(BaseModel):
    email: EmailStr
    senha: str


# Token JWT retornado após login
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

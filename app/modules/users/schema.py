from pydantic import BaseModel, EmailStr
from datetime import datetime


# Dados para criar um usuário (entrada)
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


# Dados retornados ao cliente (saída — nunca expõe a senha)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    active: bool
    created_at: datetime

    class Config:
        from_attributes = True  # Permite converter model SQLAlchemy → Pydantic


# Schema para login
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# Token JWT retornado após login
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

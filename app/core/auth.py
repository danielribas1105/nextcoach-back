from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha: str) -> str:
   return pwd_context.hash(senha)

def verificar_senha(senha_plana: str, senha_hash: str) -> bool:
   return pwd_context.verify(senha_plana, senha_hash)

def criar_token(dados: dict) -> str:
   payload = dados.copy()
   expira = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
   payload.update({"exp": expira})
   return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decodificar_token(token: str) -> dict:
   try:
      return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
   except JWTError:
      raise ValueError("Token inválido ou expirado")
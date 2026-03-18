from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.auth import decodificar_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_usuario_atual(
   token: str = Depends(oauth2_scheme),
   db: Session = Depends(get_db)
):
   credenciais_exception = HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Credenciais inválidas",
      headers={"WWW-Authenticate": "Bearer"},
   )
   try:
      payload = decodificar_token(token)
      user_id: str = payload.get("sub")
      if not user_id:
         raise credenciais_exception
   except ValueError:
      raise credenciais_exception

   # import aqui para evitar circular import
   from app.modules.user.model import User
   usuario = db.query(User).filter(User.id == user_id).first()
   if not usuario:
      raise credenciais_exception
   return usuario
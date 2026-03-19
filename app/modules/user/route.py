from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.dependencies import get_usuario_atual
from app.modules.user.schema import UserCreate, UserUpdate, UserResponse
from app.modules.user import service
from app.modules.user.model import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse, status_code=201)
def criar_usuario(dados: UserCreate, db: Session = Depends(get_db)):
    return service.criar_usuario(db, dados)


@router.get("/me", response_model=UserResponse)
def meu_perfil(usuario: User = Depends(get_usuario_atual)):
    return usuario


@router.put("/me", response_model=UserResponse)
def atualizar_perfil(
    dados: UserUpdate,
    db: Session = Depends(get_db),
    usuario: User = Depends(get_usuario_atual),
):
    return service.atualizar_usuario(db, usuario.id, dados)


@router.delete("/me", status_code=204)
def deletar_conta(
    db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)
):
    service.deletar_usuario(db, usuario.id)

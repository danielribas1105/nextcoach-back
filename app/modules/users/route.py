from fastapi import APIRouter, Depends
from app.schemas.usuario import UsuarioResponse
from app.models.usuario import Usuario
from app.dependencies import get_usuario_atual

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.get("/me", response_model=UsuarioResponse)
def meu_perfil(usuario_atual: Usuario = Depends(get_usuario_atual)):
    """Retorna os dados do usuário autenticado."""
    return usuario_atual

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.modules.user.model import User
from app.modules.user.schema import UserCreate, UsuarioResponse, LoginRequest, Token
from app.core.auth import hash_senha, verificar_senha, criar_token

router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post("/registro", response_model=UsuarioResponse, status_code=201)
def registrar(dados: UserCreate, db: Session = Depends(get_db)):
    # Verifica se e-mail já existe
    if db.query(User).filter(User.email == dados.email).first():
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")

    user = User(
        nome=dados.nome, email=dados.email, senha_hash=hash_senha(dados.senha)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", response_model=Token)
def login(dados: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == dados.email).first()

    if not user or not verificar_senha(dados.senha, user.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos",
        )

    token = criar_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

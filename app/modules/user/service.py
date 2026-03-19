from sqlalchemy.orm import Session
from app.modules.user.model import User
from app.modules.user.schema import UserCreate, UserUpdate
from app.core.auth import hash_senha
from fastapi import HTTPException


def criar_usuario(db: Session, dados: UserCreate) -> User:
    if db.query(User).filter(User.email == dados.email).first():
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")

    usuario = User(
        name=dados.name,
        email=dados.email,
        senhaHash=hash_senha(dados.senha),  # salva o hash da senha
        image=dados.image,
        weight=dados.weight,
        height=dados.height,
        age=dados.age,
        bodyFatPercentage=dados.bodyFatPercentage,
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


def buscar_por_id(db: Session, user_id: str) -> User:
    usuario = db.query(User).filter(User.id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario


def atualizar_usuario(db: Session, user_id: str, dados: UserUpdate) -> User:
    usuario = buscar_por_id(db, user_id)
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(usuario, campo, valor)
    db.commit()
    db.refresh(usuario)
    return usuario


def deletar_usuario(db: Session, user_id: str) -> None:
    usuario = buscar_por_id(db, user_id)
    db.delete(usuario)
    db.commit()

from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.modules.workout_plan.model import WorkoutPlan
from app.modules.workout_plan.schema import WorkoutPlanCreate, WorkoutPlanUpdate


def criar(db: Session, dados: WorkoutPlanCreate, user_id: str) -> WorkoutPlan:
    plano = WorkoutPlan(**dados.model_dump(), userId=user_id)
    db.add(plano)
    db.commit()
    db.refresh(plano)
    return plano


def listar(db: Session, user_id: str) -> list[WorkoutPlan]:
    return db.query(WorkoutPlan).filter(WorkoutPlan.userId == user_id).all()


def buscar(db: Session, plano_id: str, user_id: str) -> WorkoutPlan:
    plano = (
        db.query(WorkoutPlan)
        .filter(WorkoutPlan.id == plano_id, WorkoutPlan.userId == user_id)
        .first()
    )
    if not plano:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    return plano


def atualizar(
    db: Session, plano_id: str, dados: WorkoutPlanUpdate, user_id: str
) -> WorkoutPlan:
    plano = buscar(db, plano_id, user_id)
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(plano, campo, valor)
    db.commit()
    db.refresh(plano)
    return plano


def deletar(db: Session, plano_id: str, user_id: str) -> None:
    plano = buscar(db, plano_id, user_id)
    db.delete(plano)
    db.commit()

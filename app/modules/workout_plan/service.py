from sqlalchemy.orm import Session
from app.models.workout_plan import WorkoutPlan
from app.schemas.workout_plan import WorkoutPlanCreate, WorkoutPlanUpdate


def criar_workout_plan(db: Session, dados: WorkoutPlanCreate, usuario_id: int):
    plano = WorkoutPlan(**dados.model_dump(), usuario_id=usuario_id)
    db.add(plano)
    db.commit()
    db.refresh(plano)
    return plano


def listar_workout_plans(db: Session, usuario_id: int):
    return db.query(WorkoutPlan).filter(WorkoutPlan.usuario_id == usuario_id).all()


def buscar_workout_plan(db: Session, plano_id: int, usuario_id: int):
    return (
        db.query(WorkoutPlan)
        .filter(WorkoutPlan.id == plano_id, WorkoutPlan.usuario_id == usuario_id)
        .first()
    )


def atualizar_workout_plan(
    db: Session, plano_id: int, dados: WorkoutPlanUpdate, usuario_id: int
):
    plano = buscar_workout_plan(db, plano_id, usuario_id)
    if not plano:
        return None
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(plano, campo, valor)
    db.commit()
    db.refresh(plano)
    return plano


def deletar_workout_plan(db: Session, plano_id: int, usuario_id: int) -> bool:
    plano = buscar_workout_plan(db, plano_id, usuario_id)
    if not plano:
        return False
    db.delete(plano)
    db.commit()
    return True

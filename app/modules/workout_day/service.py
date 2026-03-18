from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.modules.workout_day.model import WorkoutDay
from app.modules.workout_day.schema import WorkoutDayCreate, WorkoutDayUpdate
from app.modules.workout_plan.service import buscar as buscar_plano

def criar(db: Session, plano_id: str, dados: WorkoutDayCreate, user_id: str) -> WorkoutDay:
   buscar_plano(db, plano_id, user_id)  # garante que o plano pertence ao usuário
   day = WorkoutDay(**dados.model_dump(), workoutPlanId=plano_id)
   db.add(day)
   db.commit()
   db.refresh(day)
   return day

def listar(db: Session, plano_id: str, user_id: str) -> list[WorkoutDay]:
   buscar_plano(db, plano_id, user_id)
   return db.query(WorkoutDay).filter(WorkoutDay.workoutPlanId == plano_id).all()

def buscar(db: Session, day_id: str) -> WorkoutDay:
   day = db.query(WorkoutDay).filter(WorkoutDay.id == day_id).first()
   if not day:
      raise HTTPException(status_code=404, detail="Dia de treino não encontrado")
   return day

def atualizar(db: Session, day_id: str, dados: WorkoutDayUpdate) -> WorkoutDay:
   day = buscar(db, day_id)
   for campo, valor in dados.model_dump(exclude_unset=True).items():
      setattr(day, campo, valor)
   db.commit()
   db.refresh(day)
   return day

def deletar(db: Session, day_id: str) -> None:
   day = buscar(db, day_id)
   db.delete(day)
   db.commit()
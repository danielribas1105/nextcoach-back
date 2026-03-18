from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.modules.workout_session.model import WorkoutSession
from app.modules.workout_session.schema import WorkoutSessionCreate

def registrar(db: Session, day_id: str, dados: WorkoutSessionCreate) -> WorkoutSession:
   sessao = WorkoutSession(**dados.model_dump(), workoutDayId=day_id)
   db.add(sessao)
   db.commit()
   db.refresh(sessao)
   return sessao

def listar(db: Session, day_id: str) -> list[WorkoutSession]:
   return db.query(WorkoutSession).filter(
      WorkoutSession.workoutDayId == day_id
   ).order_by(WorkoutSession.startedAt.desc()).all()

def buscar(db: Session, sessao_id: str) -> WorkoutSession:
   sessao = db.query(WorkoutSession).filter(WorkoutSession.id == sessao_id).first()
   if not sessao:
      raise HTTPException(status_code=404, detail="Sessão não encontrada")
   return sessao
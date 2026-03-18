from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.core.dependencies import get_usuario_atual
from app.modules.workout_session.schema import WorkoutSessionCreate, WorkoutSessionResponse
from app.modules.workout_session import service
from app.modules.user.model import User

router = APIRouter(
   prefix="/workout-plans/{plano_id}/days/{day_id}/sessions",
   tags=["Workout Sessions"]
)

@router.post("/", response_model=WorkoutSessionResponse, status_code=201)
def registrar(plano_id: str, day_id: str, dados: WorkoutSessionCreate, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
   return service.registrar(db, day_id, dados)

@router.get("/", response_model=List[WorkoutSessionResponse])
def listar(plano_id: str, day_id: str, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
   return service.listar(db, day_id)

@router.get("/{sessao_id}", response_model=WorkoutSessionResponse)
def buscar(plano_id: str, day_id: str, sessao_id: str, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
   return service.buscar(db, sessao_id)
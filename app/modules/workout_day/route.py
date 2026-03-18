from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.core.dependencies import get_usuario_atual
from app.modules.workout_day.schema import WorkoutDayCreate, WorkoutDayUpdate, WorkoutDayResponse
from app.modules.workout_day import service
from app.modules.user.model import User

router = APIRouter(prefix="/workout-plans/{plano_id}/days", tags=["Workout Days"])

@router.post("/", response_model=WorkoutDayResponse, status_code=201)
def criar(plano_id: str, dados: WorkoutDayCreate, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
   return service.criar(db, plano_id, dados, usuario.id)

@router.get("/", response_model=List[WorkoutDayResponse])
def listar(plano_id: str, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
   return service.listar(db, plano_id, usuario.id)

@router.get("/{day_id}", response_model=WorkoutDayResponse)
def buscar(plano_id: str, day_id: str, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
   return service.buscar(db, day_id)

@router.put("/{day_id}", response_model=WorkoutDayResponse)
def atualizar(plano_id: str, day_id: str, dados: WorkoutDayUpdate, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
   return service.atualizar(db, day_id, dados)

@router.delete("/{day_id}", status_code=204)
def deletar(plano_id: str, day_id: str, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
   service.deletar(db, day_id)
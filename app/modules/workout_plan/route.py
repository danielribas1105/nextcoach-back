from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.core.dependencies import get_usuario_atual
from app.modules.workout_plan.schema import WorkoutPlanCreate, WorkoutPlanUpdate, WorkoutPlanResponse
from app.modules.workout_plan import service
from app.modules.user.model import User

router = APIRouter(prefix="/workout-plans", tags=["Workout Plans"])

@router.post("/", response_model=WorkoutPlanResponse, status_code=201)
def criar(dados: WorkoutPlanCreate, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
    return service.criar(db, dados, usuario.id)

@router.get("/", response_model=List[WorkoutPlanResponse])
def listar(db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
    return service.listar(db, usuario.id)

@router.get("/{plano_id}", response_model=WorkoutPlanResponse)
def buscar(plano_id: str, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
    return service.buscar(db, plano_id, usuario.id)

@router.put("/{plano_id}", response_model=WorkoutPlanResponse)
def atualizar(plano_id: str, dados: WorkoutPlanUpdate, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
    return service.atualizar(db, plano_id, dados, usuario.id)

@router.delete("/{plano_id}", status_code=204)
def deletar(plano_id: str, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
    service.deletar(db, plano_id, usuario.id)
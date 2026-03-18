from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.dependencies import get_usuario_atual
from app.models.usuario import Usuario
from app.schemas.workout_plan import (
    WorkoutPlanCreate,
    WorkoutPlanUpdate,
    WorkoutPlanResponse,
)
from app.services import workout_plan as service

router = APIRouter(prefix="/workout-plans", tags=["Workout Plans"])


@router.post("/", response_model=WorkoutPlanResponse, status_code=201)
def criar(
    dados: WorkoutPlanCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_usuario_atual),
):
    return service.criar_workout_plan(db, dados, usuario.id)


@router.get("/", response_model=List[WorkoutPlanResponse])
def listar(
    db: Session = Depends(get_db), usuario: Usuario = Depends(get_usuario_atual)
):
    return service.listar_workout_plans(db, usuario.id)


@router.get("/{plano_id}", response_model=WorkoutPlanResponse)
def buscar(
    plano_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_usuario_atual),
):
    plano = service.buscar_workout_plan(db, plano_id, usuario.id)
    if not plano:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    return plano


@router.put("/{plano_id}", response_model=WorkoutPlanResponse)
def atualizar(
    plano_id: int,
    dados: WorkoutPlanUpdate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_usuario_atual),
):
    plano = service.atualizar_workout_plan(db, plano_id, dados, usuario.id)
    if not plano:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    return plano


@router.delete("/{plano_id}", status_code=204)
def deletar(
    plano_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_usuario_atual),
):
    if not service.deletar_workout_plan(db, plano_id, usuario.id):
        raise HTTPException(status_code=404, detail="Plano não encontrado")

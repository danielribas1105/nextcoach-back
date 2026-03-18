from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.core.dependencies import get_usuario_atual
from app.modules.workout_exercise.schema import WorkoutExerciseCreate, WorkoutExerciseUpdate, WorkoutExerciseResponse
from app.modules.workout_exercise import service
from app.modules.user.model import User

router = APIRouter(
   prefix="/workout-plans/{plano_id}/days/{day_id}/exercises",
   tags=["Workout Exercises"]
)

@router.post("/", response_model=WorkoutExerciseResponse, status_code=201)
def criar(plano_id: str, day_id: str, dados: WorkoutExerciseCreate, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
   return service.criar(db, day_id, dados)

@router.get("/", response_model=List[WorkoutExerciseResponse])
def listar(plano_id: str, day_id: str, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
   return service.listar(db, day_id)

@router.get("/{exercicio_id}", response_model=WorkoutExerciseResponse)
def buscar(plano_id: str, day_id: str, exercicio_id: str, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
   return service.buscar(db, exercicio_id)

@router.put("/{exercicio_id}", response_model=WorkoutExerciseResponse)
def atualizar(plano_id: str, day_id: str, exercicio_id: str, dados: WorkoutExerciseUpdate, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
   return service.atualizar(db, exercicio_id, dados)

@router.delete("/{exercicio_id}", status_code=204)
def deletar(plano_id: str, day_id: str, exercicio_id: str, db: Session = Depends(get_db), usuario: User = Depends(get_usuario_atual)):
   service.deletar(db, exercicio_id)
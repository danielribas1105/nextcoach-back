from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.modules.workout_exercise.model import WorkoutExercise
from app.modules.workout_exercise.schema import WorkoutExerciseCreate, WorkoutExerciseUpdate

def criar(db: Session, day_id: str, dados: WorkoutExerciseCreate) -> WorkoutExercise:
   exercicio = WorkoutExercise(**dados.model_dump(), workoutDayId=day_id)
   db.add(exercicio)
   db.commit()
   db.refresh(exercicio)
   return exercicio

def listar(db: Session, day_id: str) -> list[WorkoutExercise]:
   return db.query(WorkoutExercise).filter(
      WorkoutExercise.workoutDayId == day_id
   ).order_by(WorkoutExercise.order).all()

def buscar(db: Session, exercicio_id: str) -> WorkoutExercise:
   ex = db.query(WorkoutExercise).filter(WorkoutExercise.id == exercicio_id).first()
   if not ex:
      raise HTTPException(status_code=404, detail="Exercício não encontrado")
   return ex

def atualizar(db: Session, exercicio_id: str, dados: WorkoutExerciseUpdate) -> WorkoutExercise:
   ex = buscar(db, exercicio_id)
   for campo, valor in dados.model_dump(exclude_unset=True).items():
      setattr(ex, campo, valor)
   db.commit()
   db.refresh(ex)
   return ex

def deletar(db: Session, exercicio_id: str) -> None:
   ex = buscar(db, exercicio_id)
   db.delete(ex)
   db.commit()
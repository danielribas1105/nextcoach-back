from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class WorkoutExerciseCreate(BaseModel):
   name: str
   order: int
   sets: int
   reps: int
   restTimeInSeconds: int

class WorkoutExerciseUpdate(BaseModel):
   name: Optional[str] = None
   order: Optional[int] = None
   sets: Optional[int] = None
   reps: Optional[int] = None
   restTimeInSeconds: Optional[int] = None

class WorkoutExerciseResponse(BaseModel):
   id: str
   name: str
   order: int
   workoutDayId: str
   sets: int
   reps: int
   restTimeInSeconds: int
   createdAt: datetime

   class Config:
      from_attributes = True
from pydantic import BaseModel
from datetime import datetime

class WorkoutSessionCreate(BaseModel):
   startedAt: datetime
   completedAt: datetime

class WorkoutSessionResponse(BaseModel):
   id: str
   workoutDayId: str
   startedAt: datetime
   completedAt: datetime
   createdAt: datetime

   class Config:
      from_attributes = True
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.modules.workout_day.model import WeekDay

class WorkoutDayCreate(BaseModel):
   name: str
   weekDay: WeekDay
   estimatedDurationInSeconds: int
   isRest: bool = False
   coverImageUrl: Optional[str] = None

class WorkoutDayUpdate(BaseModel):
   name: Optional[str] = None
   weekDay: Optional[WeekDay] = None
   estimatedDurationInSeconds: Optional[int] = None
   isRest: Optional[bool] = None
   coverImageUrl: Optional[str] = None

class WorkoutDayResponse(BaseModel):
   id: str
   name: str
   workoutPlanId: str
   weekDay: WeekDay
   estimatedDurationInSeconds: int
   isRest: bool
   coverImageUrl: Optional[str]
   createdAt: datetime

   class Config:
      from_attributes = True
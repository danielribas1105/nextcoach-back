from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class WorkoutPlanCreate(BaseModel):
    name: str


class WorkoutPlanUpdate(BaseModel):
    name: Optional[str] = None
    isActive: Optional[bool] = None


class WorkoutPlanResponse(BaseModel):
    id: str
    name: str
    userId: str
    isActive: bool
    createdAt: datetime

    class Config:
        from_attributes = True

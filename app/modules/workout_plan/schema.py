from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class WorkoutPlanCreate(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    nivel: str
    duracao_semanas: int


class WorkoutPlanUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    nivel: Optional[str] = None
    duracao_semanas: Optional[int] = None


class WorkoutPlanResponse(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    nivel: str
    duracao_semanas: int
    usuario_id: int
    criado_em: datetime

    class Config:
        from_attributes = True

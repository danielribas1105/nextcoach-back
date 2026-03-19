import uuid

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class WorkoutSession(Base):
   __tablename__ = "workout_session"

   id           = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
   workoutDayId = Column(String, ForeignKey("workout_day.id", ondelete="CASCADE"), nullable=False)
   startedAt    = Column(DateTime(timezone=True), nullable=False)
   completedAt  = Column(DateTime(timezone=True), nullable=False)
   createdAt    = Column(DateTime(timezone=True), server_default=func.now())
   updateAt     = Column(DateTime(timezone=True), onupdate=func.now())

   workoutDay = relationship("WorkoutDay", back_populates="sessions")
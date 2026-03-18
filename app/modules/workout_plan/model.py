from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class WorkoutPlan(Base):
    __tablename__ = "workout_plan"

    id        = Column(String, primary_key=True)
    name      = Column(String, nullable=False)
    userId    = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    isActive  = Column(Boolean, default=True)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updateAt  = Column(DateTime(timezone=True), onupdate=func.now())

    user        = relationship("User", back_populates="workoutPlans")
    workoutDays = relationship("WorkoutDay", back_populates="workoutPlan", cascade="all, delete")
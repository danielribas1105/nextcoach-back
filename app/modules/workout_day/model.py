import enum
from sqlalchemy import Column, String, Boolean, DateTime, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class WeekDay(str, enum.Enum):
   SUNDAY    = "SUNDAY"
   MONDAY    = "MONDAY"
   TUESDAY   = "TUESDAY"
   WEDNESDAY = "WEDNESDAY"
   THURSDAY  = "THURSDAY"
   FRIDAY    = "FRIDAY"
   SATURDAY  = "SATURDAY"

class WorkoutDay(Base):
   __tablename__ = "WorkoutDay"

   id                         = Column(String, primary_key=True)
   name                       = Column(String, nullable=False)
   workoutPlanId              = Column(String, ForeignKey("WorkoutPlan.id", ondelete="CASCADE"), nullable=False)
   isRest                     = Column(Boolean, default=False)
   coverImageUrl              = Column(String, nullable=True)
   weekDay                    = Column(Enum(WeekDay), nullable=False)
   estimatedDurationInSeconds = Column(Integer, nullable=False)
   createdAt                  = Column(DateTime(timezone=True), server_default=func.now())
   updateAt                   = Column(DateTime(timezone=True), onupdate=func.now())

   workoutPlan = relationship("WorkoutPlan", back_populates="workoutDays")
   exercises   = relationship("WorkoutExercise", back_populates="workoutDay", cascade="all, delete")
   sessions    = relationship("WorkoutSession", back_populates="workoutDay", cascade="all, delete")
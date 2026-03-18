from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class WorkoutExercise(Base):
   __tablename__ = "WorkoutExercise"

   id                = Column(String, primary_key=True)  # ulid
   name              = Column(String, nullable=False)
   order             = Column(Integer, nullable=False)
   workoutDayId      = Column(String, ForeignKey("WorkoutDay.id", ondelete="CASCADE"), nullable=False)
   sets              = Column(Integer, nullable=False)
   reps              = Column(Integer, nullable=False)
   restTimeInSeconds = Column(Integer, nullable=False)
   createdAt         = Column(DateTime(timezone=True), server_default=func.now())
   updateAt          = Column(DateTime(timezone=True), onupdate=func.now())

   workoutDay = relationship("WorkoutDay", back_populates="exercises")
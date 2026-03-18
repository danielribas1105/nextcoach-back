from sqlalchemy import Column, String, Boolean, DateTime, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id                  = Column(String, primary_key=True)
    name                = Column(String, nullable=False)
    email               = Column(String, unique=True, nullable=False, index=True)
    emailVerified       = Column(Boolean, default=False)
    image               = Column(String, nullable=True)
    createdAt           = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt           = Column(DateTime(timezone=True), onupdate=func.now())
    weightInGrams       = Column(Integer, nullable=True)
    heightInCentimeters = Column(Integer, nullable=True)
    age                 = Column(Integer, nullable=True)
    bodyFatPercentage   = Column(Integer, nullable=True)  # 100 = 100%

    # Relacionamentos
    workoutPlans = relationship("WorkoutPlan", back_populates="user", cascade="all, delete")
    sessions     = relationship("UserSession", back_populates="user", cascade="all, delete")
    accounts     = relationship("Account", back_populates="user", cascade="all, delete")
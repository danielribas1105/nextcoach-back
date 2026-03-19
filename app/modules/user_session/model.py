import uuid

from sqlalchemy import Column, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class UserSession(Base):
   __tablename__ = "session"

   id        = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
   expiresAt = Column(DateTime(timezone=True), nullable=False)
   token     = Column(String, unique=True, nullable=False)
   createdAt = Column(DateTime(timezone=True), server_default=func.now())
   updatedAt = Column(DateTime(timezone=True), onupdate=func.now())
   ipAddress = Column(String, nullable=True)
   userAgent = Column(String, nullable=True)
   userId    = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

   user = relationship("User", back_populates="sessions")

   __table_args__ = (
      Index("ix_session_userId", "userId"),
   )
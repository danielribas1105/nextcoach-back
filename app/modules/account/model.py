import uuid

from sqlalchemy import Column, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class Account(Base):
   __tablename__ = "account"

   id                    = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
   accountId             = Column(String, nullable=False)
   providerId            = Column(String, nullable=False)
   userId                = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
   accessToken           = Column(String, nullable=True)
   refreshToken          = Column(String, nullable=True)
   idToken               = Column(String, nullable=True)
   accessTokenExpiresAt  = Column(DateTime(timezone=True), nullable=True)
   refreshTokenExpiresAt = Column(DateTime(timezone=True), nullable=True)
   scope                 = Column(String, nullable=True)
   password              = Column(String, nullable=True)
   createdAt             = Column(DateTime(timezone=True), server_default=func.now())
   updatedAt             = Column(DateTime(timezone=True), onupdate=func.now())

   user = relationship("User", back_populates="accounts")

   __table_args__ = (
      Index("ix_account_userId", "userId"),
   )
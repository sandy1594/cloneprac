 """
 Notification model.
 """

 from __future__ import annotations

 from datetime import datetime

 from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text
 from sqlalchemy.orm import Mapped, mapped_column, relationship

 from app.db.base_class import Base


 class Notification(Base):
     """Stores user notifications."""

     user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
     title: Mapped[str] = mapped_column(String(255), nullable=False)
     message: Mapped[str] = mapped_column(Text, nullable=False)
     read: Mapped[bool] = mapped_column(Boolean, default=False)
     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

     user: Mapped["User"] = relationship("User", back_populates="notifications")

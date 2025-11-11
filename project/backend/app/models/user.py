"""
User model definition.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, Enum as SAEnum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class UserRole(str, Enum):
     """Supported user roles."""

     PATIENT = "patient"
     DOCTOR = "doctor"
     ADMIN = "admin"


 class User(Base):
     """Application user."""

     name: Mapped[str] = mapped_column(String(255), nullable=False)
     email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
     phone: Mapped[str | None] = mapped_column(String(20), nullable=True)
    role: Mapped[UserRole] = mapped_column(SAEnum(UserRole), default=UserRole.PATIENT, nullable=False)
     avatar_url: Mapped[str | None] = mapped_column(String(512))
     hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
     is_active: Mapped[bool] = mapped_column(default=True)
     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

     doctor_profile: Mapped["DoctorProfile"] = relationship("DoctorProfile", back_populates="user", uselist=False)
     notifications: Mapped[list["Notification"]] = relationship("Notification", back_populates="user")
     appointments: Mapped[list["Appointment"]] = relationship(
         "Appointment", back_populates="patient", foreign_keys="Appointment.patient_id"
     )

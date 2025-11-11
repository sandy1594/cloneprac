 """
 Appointment model.
 """

 from __future__ import annotations

 from datetime import datetime
 from enum import Enum

from sqlalchemy import DateTime, Enum as PgEnum, ForeignKey, Text
 from sqlalchemy.orm import Mapped, mapped_column, relationship

 from app.db.base_class import Base


 class AppointmentStatus(str, Enum):
     """Valid statuses for appointments."""

     PENDING = "pending"
     CONFIRMED = "confirmed"
     COMPLETED = "completed"
     CANCELLED = "cancelled"


 class Appointment(Base):
     """Patient appointment data."""

     patient_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
     doctor_id: Mapped[int] = mapped_column(ForeignKey("doctorprofile.id"), nullable=False)
     scheduled_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
     status: Mapped[AppointmentStatus] = mapped_column(PgEnum(AppointmentStatus), default=AppointmentStatus.PENDING)
     reason: Mapped[str | None] = mapped_column(Text)

     patient: Mapped["User"] = relationship("User", back_populates="appointments", foreign_keys=[patient_id])
     doctor: Mapped["DoctorProfile"] = relationship("DoctorProfile", back_populates="appointments", foreign_keys=[doctor_id])
     transaction: Mapped["Transaction"] = relationship("Transaction", back_populates="appointment", uselist=False)

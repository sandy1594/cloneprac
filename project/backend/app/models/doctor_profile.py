 """
 Doctor profile model.
 """

 from __future__ import annotations

 from datetime import datetime

 from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String
 from sqlalchemy.orm import Mapped, mapped_column, relationship

 from app.db.base_class import Base


 class DoctorProfile(Base):
     """Doctor-specific details."""

     user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), unique=True, nullable=False)
     specialty_id: Mapped[int] = mapped_column(ForeignKey("specialty.id"), nullable=False)
     experience_years: Mapped[int] = mapped_column(Integer, default=0)
     bio: Mapped[str | None] = mapped_column(String(1000))
     clinic_name: Mapped[str | None] = mapped_column(String(255))
     clinic_address: Mapped[str | None] = mapped_column(String(1024))
     fee: Mapped[float | None] = mapped_column(Float)
     rating: Mapped[float | None] = mapped_column(Float)
     verified: Mapped[bool] = mapped_column(Boolean, default=False)
     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

     user: Mapped["User"] = relationship("User", back_populates="doctor_profile")
     specialty: Mapped["Specialty"] = relationship("Specialty", back_populates="doctors")
     appointments: Mapped[list["Appointment"]] = relationship(
         "Appointment", back_populates="doctor", foreign_keys="Appointment.doctor_id"
     )

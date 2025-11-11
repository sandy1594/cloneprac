 """
 Medical specialty model.
 """

 from __future__ import annotations

 from sqlalchemy import String, Text
 from sqlalchemy.orm import Mapped, mapped_column, relationship

 from app.db.base_class import Base


 class Specialty(Base):
     """Medical specialty metadata."""

     name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
     description: Mapped[str | None] = mapped_column(Text)

     doctors: Mapped[list["DoctorProfile"]] = relationship("DoctorProfile", back_populates="specialty")

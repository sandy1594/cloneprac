 """
 Payment transaction model.
 """

 from __future__ import annotations

 from enum import Enum

from sqlalchemy import Enum as PgEnum, Float, ForeignKey, String
 from sqlalchemy.orm import Mapped, mapped_column, relationship

 from app.db.base_class import Base


 class TransactionStatus(str, Enum):
     """Valid transaction status values."""

     PENDING = "pending"
     COMPLETED = "completed"
     FAILED = "failed"
     REFUNDED = "refunded"


 class PaymentMethod(str, Enum):
     """Supported payment methods."""

     CARD = "card"
     UPI = "upi"
     CASH = "cash"
     WALLET = "wallet"


 class Transaction(Base):
     """Payment record tied to an appointment."""

     appointment_id: Mapped[int] = mapped_column(ForeignKey("appointment.id"), unique=True, nullable=False)
     amount: Mapped[float] = mapped_column(Float, nullable=False)
     currency: Mapped[str] = mapped_column(String(3), default="INR")
     status: Mapped[TransactionStatus] = mapped_column(PgEnum(TransactionStatus), default=TransactionStatus.PENDING)
     payment_method: Mapped[PaymentMethod] = mapped_column(PgEnum(PaymentMethod), default=PaymentMethod.CARD)

     appointment: Mapped["Appointment"] = relationship("Appointment", back_populates="transaction")

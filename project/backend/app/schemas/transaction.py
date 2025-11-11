 """
 Schemas for payment transactions.
 """

 from pydantic import BaseModel

 from app.models.transaction import PaymentMethod, TransactionStatus


 class TransactionBase(BaseModel):
     """Shared transaction attributes."""

     appointment_id: int
     amount: float
     currency: str = "INR"
     payment_method: PaymentMethod = PaymentMethod.CARD


 class TransactionCreate(TransactionBase):
     """Creation payload."""

     status: TransactionStatus = TransactionStatus.PENDING


 class TransactionRead(TransactionBase):
     """Response schema."""

     id: int
     status: TransactionStatus

     class Config:
         from_attributes = True

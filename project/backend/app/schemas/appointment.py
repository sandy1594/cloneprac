 """
 Appointment-related schemas.
 """

 from datetime import datetime
 from typing import Optional

 from pydantic import BaseModel

 from app.models.appointment import AppointmentStatus


 class AppointmentBase(BaseModel):
     """Shared appointment fields."""

     doctor_id: int
     scheduled_time: datetime
     reason: Optional[str] = None


class AppointmentBookRequest(AppointmentBase):
    """Patient-facing payload for booking."""

    pass


 class AppointmentCreate(AppointmentBase):
     """Payload to create an appointment."""

     patient_id: int


 class AppointmentRead(AppointmentBase):
     """Response returned to clients."""

     id: int
     patient_id: int
     status: AppointmentStatus

     class Config:
         from_attributes = True


 class AppointmentUpdateStatus(BaseModel):
     """Schema for updating appointment status."""

     status: AppointmentStatus

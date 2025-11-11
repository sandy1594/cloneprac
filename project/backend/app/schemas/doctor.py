 """
 Schemas for doctor profiles and availability.
 """

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


 class DoctorProfileBase(BaseModel):
     """Shared doctor profile fields."""

     specialty_id: int
     experience_years: int
     bio: Optional[str] = None
     clinic_name: Optional[str] = None
     clinic_address: Optional[str] = None
     fee: Optional[float] = None


class DoctorProfileCreate(DoctorProfileBase):
     """Create payload requiring user reference."""

    user_id: Optional[int] = None


 class DoctorProfileUpdate(BaseModel):
     """Fields that can be updated by doctor/admin."""

     specialty_id: Optional[int] = None
     experience_years: Optional[int] = None
     bio: Optional[str] = None
     clinic_name: Optional[str] = None
     clinic_address: Optional[str] = None
     fee: Optional[float] = None
     verified: Optional[bool] = None


 class DoctorProfileRead(DoctorProfileBase):
     """Response schema."""

     id: int
     user_id: int
     rating: Optional[float] = None
     verified: bool
     created_at: datetime

     class Config:
         from_attributes = True


 class AvailabilitySlot(BaseModel):
     """Represents doctor availability window."""

     start_time: datetime
     end_time: datetime
     is_available: bool = True


class DoctorAvailabilityUpdate(BaseModel):
    """Payload for updating doctor availability slots."""

    slots: List[AvailabilitySlot]

 """
 Doctor-facing routes.
 """

 from typing import List

 from fastapi import APIRouter, Depends, HTTPException, status
 from sqlalchemy.orm import Session

 from app.api import deps
 from app.models.appointment import Appointment
 from app.models.doctor_profile import DoctorProfile
 from app.models.user import User, UserRole
from app.schemas import AppointmentRead, DoctorAvailabilityUpdate, DoctorProfileCreate, DoctorProfileRead
 from app.services import availability

 router = APIRouter()


 def _ensure_doctor_role(user: User) -> None:
     if user.role != UserRole.DOCTOR:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only doctors can access this resource")


 @router.post("/profile", response_model=DoctorProfileRead, summary="Create or update doctor profile")
 def upsert_profile(
     payload: DoctorProfileCreate,
     current_user: User = Depends(deps.get_current_active_user),
     db: Session = Depends(deps.get_db),
 ) -> DoctorProfile:
     """Allow doctors to create or update their profile."""
     _ensure_doctor_role(current_user)

     profile = db.query(DoctorProfile).filter(DoctorProfile.user_id == current_user.id).first()

     if profile:
         update_data = payload.dict(exclude_unset=True, exclude_none=True)
         for field, value in update_data.items():
             if field == "user_id":
                 continue
             setattr(profile, field, value)
     else:
         if payload.specialty_id is None:
             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="specialty_id is required")
         profile = DoctorProfile(
             user_id=current_user.id,
             specialty_id=payload.specialty_id,
             experience_years=payload.experience_years,
             bio=payload.bio,
             clinic_name=payload.clinic_name,
             clinic_address=payload.clinic_address,
             fee=payload.fee,
         )
         db.add(profile)

     db.commit()
     db.refresh(profile)
     return profile


 @router.get("/appointments", response_model=List[AppointmentRead], summary="List doctor appointments")
 def list_doctor_appointments(
     current_user: User = Depends(deps.get_current_active_user),
     db: Session = Depends(deps.get_db),
 ) -> List[Appointment]:
     """Return appointments for the current doctor."""
     _ensure_doctor_role(current_user)

     profile = db.query(DoctorProfile).filter(DoctorProfile.user_id == current_user.id).first()
     if not profile:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor profile not found")

     return (
         db.query(Appointment)
         .filter(Appointment.doctor_id == profile.id)
         .order_by(Appointment.scheduled_time.desc())
         .all()
     )


 @router.put("/availability", summary="Update availability schedule")
 def update_availability(
     payload: DoctorAvailabilityUpdate,
     current_user: User = Depends(deps.get_current_active_user),
     db: Session = Depends(deps.get_db),
 ) -> dict:
     """Store availability slots for the doctor (placeholder implementation)."""
     _ensure_doctor_role(current_user)

     profile = db.query(DoctorProfile).filter(DoctorProfile.user_id == current_user.id).first()
     if not profile:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor profile not found")

     stored_slots = availability.set_availability(profile.id, payload.slots)
     return {"doctor_profile_id": profile.id, "slots": stored_slots}

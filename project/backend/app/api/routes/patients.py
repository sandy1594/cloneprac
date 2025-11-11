 """
 Patient-facing routes.
 """

 from typing import List, Optional

 from fastapi import APIRouter, Depends, HTTPException, Query, status
 from sqlalchemy.orm import Session

 from app.api import deps
 from app.models.appointment import Appointment, AppointmentStatus
 from app.models.doctor_profile import DoctorProfile
 from app.models.user import User, UserRole
 from app.schemas import AppointmentBookRequest, AppointmentRead, DoctorProfileRead

 router = APIRouter()


 @router.get(
     "/doctors",
     response_model=List[DoctorProfileRead],
     summary="Search doctors by specialty, symptoms, or location",
 )
 def list_doctors(
     specialty: Optional[int] = Query(default=None, description="Filter by specialty id"),
     location: Optional[str] = Query(default=None, description="Filter by clinic address"),
     query: Optional[str] = Query(default=None, description="Free text search over name/bio"),
     db: Session = Depends(deps.get_db),
 ) -> List[DoctorProfile]:
     """Return doctors matching filters."""
     q = db.query(DoctorProfile).join(DoctorProfile.user).outerjoin(DoctorProfile.specialty)

     if specialty:
         q = q.filter(DoctorProfile.specialty_id == specialty)
     if location:
         ilike_pattern = f"%{location.lower()}%"
         q = q.filter(DoctorProfile.clinic_address.ilike(ilike_pattern))
     if query:
         ilike_pattern = f"%{query.lower()}%"
         q = q.filter(
             (DoctorProfile.bio.ilike(ilike_pattern))
             | (DoctorProfile.clinic_name.ilike(ilike_pattern))
             | (DoctorProfile.user.has(User.name.ilike(ilike_pattern)))
         )

     return q.limit(50).all()


 @router.get("/doctors/{doctor_id}", response_model=DoctorProfileRead, summary="Get doctor profile detail")
 def get_doctor_profile(doctor_id: int, db: Session = Depends(deps.get_db)) -> DoctorProfile:
     """Fetch a single doctor profile."""
     doctor = db.query(DoctorProfile).filter(DoctorProfile.id == doctor_id).first()
     if not doctor:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found")
     return doctor


 @router.post(
     "/appointments",
     response_model=AppointmentRead,
     status_code=status.HTTP_201_CREATED,
     summary="Book an appointment with a doctor",
 )
 def book_appointment(
     payload: AppointmentBookRequest,
     current_user: User = Depends(deps.get_current_active_user),
     db: Session = Depends(deps.get_db),
 ) -> Appointment:
     """Create an appointment for the current patient."""
     if current_user.role != UserRole.PATIENT:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only patients can book appointments")

     doctor = db.query(DoctorProfile).filter(DoctorProfile.id == payload.doctor_id).first()
     if not doctor:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found")

     appointment = Appointment(
         patient_id=current_user.id,
         doctor_id=payload.doctor_id,
         scheduled_time=payload.scheduled_time,
         reason=payload.reason,
         status=AppointmentStatus.PENDING,
     )
     db.add(appointment)
     db.commit()
     db.refresh(appointment)
     return appointment


 @router.get(
     "/appointments",
     response_model=List[AppointmentRead],
     summary="List appointments for current patient",
 )
 def list_patient_appointments(
     current_user: User = Depends(deps.get_current_active_user),
     db: Session = Depends(deps.get_db),
 ) -> List[Appointment]:
     """Return appointments belonging to the current patient."""
     if current_user.role != UserRole.PATIENT:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only patients can view this resource")

     return (
         db.query(Appointment)
         .filter(Appointment.patient_id == current_user.id)
         .order_by(Appointment.scheduled_time.desc())
         .all()
     )

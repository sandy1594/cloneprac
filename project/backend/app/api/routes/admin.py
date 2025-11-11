 """
 Administrative routes.
 """

 from typing import Dict, List

from fastapi import APIRouter, Depends, HTTPException
 from sqlalchemy import func
 from sqlalchemy.orm import Session

 from app.api import deps
 from app.models.appointment import Appointment, AppointmentStatus
 from app.models.doctor_profile import DoctorProfile
 from app.models.transaction import Transaction, TransactionStatus
 from app.models.user import User, UserRole
 from app.schemas import DoctorProfileRead

 router = APIRouter()


 def _ensure_admin_role(user: User) -> None:
     if user.role != UserRole.ADMIN:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")


 @router.get(
     "/doctors/pending-verification",
     response_model=List[DoctorProfileRead],
     summary="List doctors awaiting verification",
 )
 def list_pending_doctors(
     current_user: User = Depends(deps.get_current_active_user),
     db: Session = Depends(deps.get_db),
 ) -> List[DoctorProfile]:
     """Return doctor profiles that have not yet been verified."""
     _ensure_admin_role(current_user)
     return (
         db.query(DoctorProfile)
         .filter(DoctorProfile.verified.is_(False))
         .order_by(DoctorProfile.created_at.asc())
         .all()
     )


 @router.put("/doctors/{doctor_id}/verify", response_model=DoctorProfileRead, summary="Verify a doctor profile")
 def verify_doctor(
     doctor_id: int,
     current_user: User = Depends(deps.get_current_active_user),
     db: Session = Depends(deps.get_db),
 ) -> DoctorProfile:
     """Mark a doctor profile as verified."""
     _ensure_admin_role(current_user)

     profile = db.query(DoctorProfile).filter(DoctorProfile.id == doctor_id).first()
     if not profile:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor profile not found")

     profile.verified = True
     db.commit()
     db.refresh(profile)
     return profile


 @router.get("/analytics", summary="High-level platform metrics")
 def get_analytics(
     current_user: User = Depends(deps.get_current_active_user),
     db: Session = Depends(deps.get_db),
 ) -> Dict[str, object]:
     """Return aggregate metrics for admin dashboards."""
     _ensure_admin_role(current_user)

     total_users = db.query(func.count(User.id)).scalar() or 0
     total_doctors = db.query(func.count(DoctorProfile.id)).scalar() or 0
     pending_verifications = db.query(func.count(DoctorProfile.id)).filter(DoctorProfile.verified.is_(False)).scalar() or 0
     total_appointments = db.query(func.count(Appointment.id)).scalar() or 0
     appointments_by_status = {
         status.value: db.query(func.count(Appointment.id)).filter(Appointment.status == status).scalar() or 0
         for status in AppointmentStatus
     }
     total_revenue = (
         db.query(func.coalesce(func.sum(Transaction.amount), 0.0))
         .filter(Transaction.status == TransactionStatus.COMPLETED)
         .scalar()
         or 0.0
     )

     return {
         "users": {"total": total_users},
         "doctors": {"total": total_doctors, "pending_verification": pending_verifications},
         "appointments": {"total": total_appointments, "by_status": appointments_by_status},
         "payments": {"total_revenue": float(total_revenue)},
     }

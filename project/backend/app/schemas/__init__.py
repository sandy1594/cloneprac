 """Aggregate schema imports for convenience."""

from .appointment import AppointmentBookRequest, AppointmentCreate, AppointmentRead, AppointmentUpdateStatus
 from .auth import LoginRequest
from .doctor import DoctorAvailabilityUpdate, DoctorProfileCreate, DoctorProfileRead, DoctorProfileUpdate
 from .notification import NotificationCreate, NotificationRead
 from .token import Token, TokenPayload
 from .transaction import TransactionCreate, TransactionRead
 from .user import UserCreate, UserRead, UserUpdate

 __all__ = [
    "AppointmentBookRequest",
    "AppointmentCreate",
     "AppointmentRead",
     "AppointmentUpdateStatus",
     "LoginRequest",
    "DoctorProfileCreate",
     "DoctorProfileRead",
     "DoctorProfileUpdate",
    "DoctorAvailabilityUpdate",
     "NotificationCreate",
     "NotificationRead",
     "Token",
     "TokenPayload",
     "TransactionCreate",
     "TransactionRead",
     "UserCreate",
     "UserRead",
     "UserUpdate",
 ]

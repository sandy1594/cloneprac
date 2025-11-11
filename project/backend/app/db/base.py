 """
 Import models for Alembic autogeneration.
 """

 from app.db.base_class import Base  # noqa: F401
 from app.models.appointment import Appointment  # noqa: F401
 from app.models.doctor_profile import DoctorProfile  # noqa: F401
 from app.models.notification import Notification  # noqa: F401
 from app.models.specialty import Specialty  # noqa: F401
 from app.models.transaction import Transaction  # noqa: F401
 from app.models.user import User  # noqa: F401

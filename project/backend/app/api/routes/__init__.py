 """
 Aggregate FastAPI routers.
 """

 from fastapi import APIRouter

 from app.api.routes import admin, auth, doctors, patients

 api_router = APIRouter()

 api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
 api_router.include_router(patients.router, tags=["Patients"])
 api_router.include_router(doctors.router, prefix="/doctor", tags=["Doctor"])
 api_router.include_router(admin.router, prefix="/admin", tags=["Admin"])

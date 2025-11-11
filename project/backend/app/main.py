 """
 Entry point for the FastAPI application.
 """

 from fastapi import FastAPI
 from fastapi.middleware.cors import CORSMiddleware

 from app.api.routes import api_router
 from app.core.config import settings


 def create_application() -> FastAPI:
     """Create and configure the FastAPI application instance."""
     app = FastAPI(
         title=settings.PROJECT_NAME,
         version=settings.VERSION,
         openapi_url=f"{settings.API_PREFIX}/openapi.json",
         docs_url=f"{settings.API_PREFIX}/docs",
     )

     app.add_middleware(
         CORSMiddleware,
         allow_origins=settings.BACKEND_CORS_ORIGINS,
         allow_credentials=True,
         allow_methods=["*"],
         allow_headers=["*"],
     )

     app.include_router(api_router, prefix=settings.API_PREFIX)

     return app


 app = create_application()

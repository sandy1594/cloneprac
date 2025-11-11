 """
 Application configuration using environment variables.
 """

 from functools import lru_cache
 from typing import List

 from pydantic_settings import BaseSettings, SettingsConfigDict


 class Settings(BaseSettings):
     """Application settings loaded from environment variables."""

     model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", env_prefix="APP_")

     PROJECT_NAME: str = "Healthcare Platform API"
     VERSION: str = "0.1.0"
     API_PREFIX: str = "/api"

     # Security
     SECRET_KEY: str = "change-me"
     ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
     ALGORITHM: str = "HS256"

     # Database
     DATABASE_URL: str = "postgresql+psycopg://postgres:postgres@localhost:5432/healthcare"

     # CORS
     BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]

     # Redis
     REDIS_URL: str = "redis://localhost:6379/0"


 @lru_cache
 def get_settings() -> Settings:
     """Return cached settings instance."""
     return Settings()


 settings = get_settings()

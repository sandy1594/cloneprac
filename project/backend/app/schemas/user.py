 """
 Pydantic schemas for user resources.
 """

 from datetime import datetime
 from typing import Optional

 from pydantic import BaseModel, EmailStr, HttpUrl

 from app.models.user import UserRole


 class UserBase(BaseModel):
     """Shared user attributes."""

     name: str
     email: EmailStr
     phone: Optional[str] = None
     role: UserRole = UserRole.PATIENT
     avatar_url: Optional[HttpUrl] = None


 class UserCreate(UserBase):
     """Schema for user registration."""

     password: str


 class UserUpdate(BaseModel):
     """Schema for updating profile details."""

     name: Optional[str] = None
     phone: Optional[str] = None
     avatar_url: Optional[HttpUrl] = None


 class UserRead(UserBase):
     """Schema returned to clients."""

     id: int
     created_at: datetime

     class Config:
         from_attributes = True

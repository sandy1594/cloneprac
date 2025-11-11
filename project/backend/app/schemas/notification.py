 """
 Notification schemas.
 """

 from datetime import datetime

 from pydantic import BaseModel


 class NotificationBase(BaseModel):
     """Shared notification fields."""

     title: str
     message: str


 class NotificationCreate(NotificationBase):
     """Payload to create notification."""

     user_id: int


 class NotificationRead(NotificationBase):
     """Response schema."""

     id: int
     user_id: int
     read: bool
     created_at: datetime

     class Config:
         from_attributes = True

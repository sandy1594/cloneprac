 """
 Schemas representing medical specialties.
 """

 from typing import Optional

 from pydantic import BaseModel


 class SpecialtyBase(BaseModel):
     """Shared specialty fields."""

     name: str
     description: Optional[str] = None


 class SpecialtyCreate(SpecialtyBase):
     """Payload for creating a specialty."""

     pass


 class SpecialtyRead(SpecialtyBase):
     """Response schema."""

     id: int

     class Config:
         from_attributes = True

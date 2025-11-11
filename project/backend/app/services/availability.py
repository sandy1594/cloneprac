 """
 In-memory placeholder service for doctor availability.
 
 This should later be replaced with persistence in the database or an external
 scheduling system. For now it keeps availability windows per doctor in a simple
 dictionary so that the API remains functional for prototyping.
 """

 from __future__ import annotations

 from collections import defaultdict
 from typing import Dict, List

 from app.schemas.doctor import AvailabilitySlot

 _availability_store: Dict[int, List[AvailabilitySlot]] = defaultdict(list)


 def set_availability(doctor_id: int, slots: List[AvailabilitySlot]) -> List[AvailabilitySlot]:
     """Persist availability slots for a doctor."""
     _availability_store[doctor_id] = slots
     return slots


 def get_availability(doctor_id: int) -> List[AvailabilitySlot]:
     """Return previously stored availability slots."""
     return _availability_store.get(doctor_id, [])

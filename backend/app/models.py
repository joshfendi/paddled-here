from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class Coordinates(BaseModel):
    lat: float
    lng: float

class PaddleLocation(BaseModel):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    user_name: str
    event_name: str
    team: Optional[str]
    location_name: str
    coordinates: Coordinates
    date: date
    notes: Optional[str]
    photo_url: Optional[str]

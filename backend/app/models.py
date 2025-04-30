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

class PaddleUpdate(BaseModel):
    user_name: Optional[str] = None
    event_name: Optional[str] = None
    team: Optional[str] = None
    location_name: Optional[str] = None
    coordinates: Optional[Coordinates] = None
    date: Optional[date] = None
    notes: Optional[str] = None
    photo_url: Optional[str] = None

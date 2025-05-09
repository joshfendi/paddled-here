from sqlmodel import SQLModel, Field, Column, JSON
from typing import Optional, List
from datetime import date as dt_date, datetime
from pydantic import BaseModel

# Use Pydantic BaseModel for nested structure
class Coordinates(BaseModel):
    lat: float
    lng: float

class PaddleLocation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    user_name: str
    event_name: str
    team: Optional[str]
    location_name: str
    coordinates: Coordinates = Field(sa_column=Column(JSON))  # stored as JSON
    date: dt_date
    notes: Optional[str]
    photo_url: Optional[str]

class PaddleUpdate(SQLModel):
    user_name: Optional[str] = None
    event_name: Optional[str] = None
    team: Optional[str] = None
    location_name: Optional[str] = None
    coordinates: Optional[Coordinates] = None
    date: Optional[dt_date] = None
    notes: Optional[str] = None
    photo_url: Optional[str] = None

# Define this AFTER PaddleLocation is declared
class PaddlesPage(SQLModel):
    total: int
    results: List[PaddleLocation]
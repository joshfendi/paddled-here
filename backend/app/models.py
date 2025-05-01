from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date as dt_date, datetime

class Coordinates(SQLModel):
    lat: float
    lng: float

class PaddleLocation(SQLModel, table=True):  # 👈 makes it a SQL table
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    user_name: str
    event_name: str
    team: Optional[str]
    location_name: str
    coordinates: Coordinates
    date: dt_date
    notes: Optional[str]
    photo_url: Optional[str]

class PaddleUpdate(SQLModel):  # no table=True = this is not a table, just used for PATCH
    user_name: Optional[str] = None
    event_name: Optional[str] = None
    team: Optional[str] = None
    location_name: Optional[str] = None
    coordinates: Optional[Coordinates] = None
    date: Optional[dt_date] = None
    notes: Optional[str] = None
    photo_url: Optional[str] = None

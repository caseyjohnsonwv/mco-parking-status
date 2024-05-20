from datetime import datetime
from sqlalchemy import func as F
from sqlalchemy.orm import Mapped, mapped_column, validates
from db import Base
from .enum import ParkingStatus


class ParkingLocation(Base):
    __tablename__ = 'parking_location'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    status: Mapped[str]
    daily_rate_usd: Mapped[float]
    last_updated_datetime: Mapped[datetime] = mapped_column(server_default=F.now())
    
    def __repr__(self:"ParkingLocation") -> str:
        return f"<<{self.name}: {self.status} ({self.last_updated_datetime.isoformat()})>>"
    
    @validates('status')
    def validate_status(self, key, value:str):
        parking_status = ParkingStatus.interpolate(value)
        return parking_status.value

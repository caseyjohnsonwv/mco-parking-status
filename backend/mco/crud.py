from typing import List
from db import PostgresWrapper
from .models import ParkingLocation
from .enum import ParkingStatus
from log import get_logger
from sqlalchemy.orm import Session

logger = get_logger(__name__)

class CrudUtils:    
    def get_parking_locations(status: ParkingStatus = None) -> List[ParkingLocation]:
        with PostgresWrapper.connect() as session:
            assert isinstance(session, Session)
            query = session.query(ParkingLocation)
            if status:
                query = query.filter(ParkingLocation.status == status.value)
            results = query.all()
        return results

    def reload_parking_locations(locations: List[ParkingLocation]):
        with PostgresWrapper.connect() as session:
            assert isinstance(session, Session)
            session.query(ParkingLocation).delete()
            session.add_all(locations)
            session.commit()

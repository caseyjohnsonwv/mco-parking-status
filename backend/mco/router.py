from datetime import datetime
from typing import List
from fastapi import Response, status as StatusCode
from fastapi.routing import APIRouter
from pydantic import BaseModel
from .crud import CrudUtils
from .enum import ParkingStatus
from .models import ParkingLocation as ParkingLocationModel
from log import get_logger


router = APIRouter(prefix='/mco')
logger = get_logger(__name__)


class ParkingLocation(BaseModel):
    name: str
    status: str
    daily_rate_usd: float
    last_updated_datetime: datetime
    def from_db_model(model:ParkingLocationModel) -> "ParkingLocation":
        return ParkingLocation(
            name=model.name,
            status=model.status,
            daily_rate_usd=model.daily_rate_usd,
            last_updated_datetime=model.last_updated_datetime
        )

class ParkingStatusResponse(BaseModel):
    locations: List[ParkingLocation]


@router.get('/')
async def get_parking_locations(status:str=None):
    parking_status = ParkingStatus.interpolate(status) if status else None
    results = CrudUtils.get_parking_locations(status=parking_status)
    locations = [ParkingLocation.from_db_model(r) for r in results]
    response = ParkingStatusResponse(locations=locations)
    return Response(response.model_dump_json(), status_code=StatusCode.HTTP_200_OK)

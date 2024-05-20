from enum import Enum

class ParkingStatus(Enum):
    CLOSED = 'CLOSED'
    FULL = 'FULL'
    OPEN = 'OPEN'
    UNKNOWN = 'UNKNOWN'
    
    @classmethod
    def interpolate(cls, value:str) -> "ParkingStatus":
        for v,item in cls._value2member_map_.items():
            if str(v).lower() == value.lower():
                return item
        return ParkingStatus.UNKNOWN

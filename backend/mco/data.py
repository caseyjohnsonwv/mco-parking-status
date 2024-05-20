import re
from typing import List
from bs4 import BeautifulSoup
import requests
from .crud import CrudUtils
from .enum import ParkingStatus
from .models import ParkingLocation
from log import get_logger


BASE_URL = 'https://orlandoairports.net/parking-transportation/parking/'
logger = get_logger(__name__)


class DataWrapper:
    def refresh_data():
        logger.info(f"Refreshing data from {BASE_URL}")
        resp = requests.get(BASE_URL)
        soup = BeautifulSoup(resp.text, features='html.parser')
        summary_table = soup.find('section', attrs={'id':'parking-rates'}).find('table')
        locations: List[ParkingLocation] = []
        for tr in summary_table.find_all('tr'):
            name, price, status = [e.get_text() for e in tr.find_all('td')]
            # get parking rate - if multiple, it's a range like $20-$30, so take the last one
            daily_rate_usd = re.findall('\$(\d+(?:\.\d{2})?)', price)[-1] if str(price).upper() != 'FREE' else 0
            # convert empty statuses to OPEN
            status_name = ParkingStatus.interpolate(status).value if len(status) > 0 else ParkingStatus.OPEN.value
            # save for bulk truncate/reload
            locations.append(ParkingLocation(name=name, status=status_name, daily_rate_usd=daily_rate_usd))
        # do truncate/reload
        logger.info(f"Found data for {len(locations)} parking locations")
        CrudUtils.reload_parking_locations(locations)

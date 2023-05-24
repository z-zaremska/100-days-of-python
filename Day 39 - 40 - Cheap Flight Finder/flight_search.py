import requests
import os
import datetime as dt


KIWI_LOCATIONS_URL = 'https://api.tequila.kiwi.com/locations/query'
KIWI_API_KEY = os.environ.get('KIWI_API_KEY')
today = dt.date.today().strftime('%d/%m/%Y')

KIWI_LOCATIONS_HEADERS = {
    'apikey': KIWI_API_KEY
}

KIWI_LOCATIONS_PARAMS = {
    'location_types': 'airport',
    'limit': 1,
    'term': ''
}


class FlightSearch:
    """Class using locations API."""
    def __init__(self, location):
        self.location = location
        self.iata_code = self.get_iata_code()

    def get_iata_code(self):
        """Returns IATA code using location name."""
        KIWI_LOCATIONS_PARAMS['term'] = self.location
        search_response = requests.get(
            url=KIWI_LOCATIONS_URL,
            params=KIWI_LOCATIONS_PARAMS,
            headers=KIWI_LOCATIONS_HEADERS
        )
        search_response.raise_for_status()
        iata_code = search_response.json()['locations'][0]['city']['code']

        return iata_code

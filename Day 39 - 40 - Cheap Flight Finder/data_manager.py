from flight_search import FlightSearch
import requests
import os

MY_FLIGHTS_URL = 'https://api.sheety.co/3940615f01c64bc132046d75bfe21c84/flightDeals/prices'
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
SHEETY_HEADERS = {'Authorization': SHEETY_TOKEN}


class DataManager:
    """Class responsible for communication with Flights Google Sheet. """
    def __init__(self):
        self.destinations = requests.get(url=MY_FLIGHTS_URL, headers=SHEETY_HEADERS).json()['prices']
        self.get_city_codes()
        self.save_city_codes()

    def get_city_codes(self):
        for destination in self.destinations:
            if destination['iataCode'] == '':
                city_name = destination['city']
                destination['iataCode'] = FlightSearch(city_name).iata_code

    def save_city_codes(self):
        """Insert missing IATA codes to Flights Google Sheet."""
        for destination in self.destinations:
            row_body = {
                'price': {
                    'iataCode': destination['iataCode']
                }
            }
            requests.put(url=f'{MY_FLIGHTS_URL}/{destination["id"]}', json=row_body, headers=SHEETY_HEADERS)

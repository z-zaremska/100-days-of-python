import requests
from flight_data import FlightData


KIWI_LOCATIONS_URL = 'https://api.tequila.kiwi.com/locations/query'
KIWI_SEARCH_URL = 'https://api.tequila.kiwi.com/v2/search'

KIWI_HEADERS = {
    'apikey': 'your_api_key'
}

KIWI_LOCATIONS_PARAMS = {
    'location_types': 'airport',
    'limit': 1,
    'term': '',
    'flight_type': 'oneway'
}


class FlightSearch:
    """Class responsible for communication with KIWI locations API."""

    def __init__(self, kiwi_api_key):
        KIWI_HEADERS['apikey'] = kiwi_api_key

    @staticmethod
    def get_iata_code(location):
        """Returns IATA code using location name."""
        KIWI_LOCATIONS_PARAMS['term'] = location
        location_response = requests.get(
            url=KIWI_LOCATIONS_URL,
            params=KIWI_LOCATIONS_PARAMS,
            headers=KIWI_HEADERS
        )
        location_response.raise_for_status()
        iata_code = location_response.json()['locations'][0]['city']['code']

        return iata_code
    
    @staticmethod
    def check_flights(origin_city_code, destination_city_code, from_time, to_time):
        data_input = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "PLN"
        }

        flight = requests.get(url=KIWI_SEARCH_URL, params=data_input, headers=KIWI_HEADERS)

        try:
            data = flight.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")

        return flight_data

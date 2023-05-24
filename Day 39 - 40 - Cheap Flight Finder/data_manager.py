import requests

SHEETY_HEADERS = {'Authorization': 'your_token'}


class DataManager:
    """Class responsible for communication with Flights Google Sheet. """
    def __init__(self, sheety_token, sheety_url):
        SHEETY_HEADERS['Authorization'] = sheety_token
        self.sheety_token = sheety_token,
        self.sheety_url = sheety_url
        self.destinations = requests.get(url=sheety_url, headers=SHEETY_HEADERS).json()['prices']

    def save_iata_codes(self):
        """Save IATA Codes in the Flights Google Sheet."""
        for destination in self.destinations:
            updated_row = {
                'price': {'iataCode': destination['iataCode']}
            }
            requests.put(url=f'{self.sheety_url}/{destination["id"]}', json=updated_row, headers=SHEETY_HEADERS)

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt
from dateutil.relativedelta import relativedelta
import os


MY_FLIGHTS_URL = 'https://api.sheety.co/3940615f01c64bc132046d75bfe21c84/flightDeals/prices'
ORIGIN_CITY_CODE = 'GDN'
SEARCH_START = dt.datetime.today() + dt.timedelta(days=1)
SEARCH_END = SEARCH_START + relativedelta(months=6)


data_manager = DataManager(
    os.environ.get('SHEETY_TOKEN'),
    MY_FLIGHTS_URL
)
flight_search = FlightSearch(
    os.environ.get('KIWI_API_KEY')
)
notification_manager = NotificationManager()


# Check if all destinations has their IATA Code - is not, find one.
for destination in data_manager.destinations:
    if destination['iataCode'] == '':
        city_name = destination['city']
        destination['iataCode'] = flight_search.get_iata_code(city_name)

# Save found IATA Codes to Flight Google Sheet.
data_manager.save_iata_codes()

# For each destination check flights
for destination in data_manager.destinations:
    destination_city_code = destination['iataCode']
    flight = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        destination_city_code,
        SEARCH_START,
        SEARCH_END
    )

    try:
        if flight.price < destination["lowestPrice"]:
            print('Lower price')
            notification_manager.send_sms(
                message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            )
    except AttributeError:
        pass

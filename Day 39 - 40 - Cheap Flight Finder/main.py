from data_manager import DataManager
from user_manager import UserManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt
from dateutil.relativedelta import relativedelta
import os


MY_FLIGHTS_URL = 'https://api.sheety.co/3940615f01c64bc132046d75bfe21c84/flightDeals/prices'
USERS_URL = 'https://api.sheety.co/3940615f01c64bc132046d75bfe21c84/flightDeals/users'
ORIGIN_CITY_CODE = 'GDN'
SEARCH_START = dt.datetime.today() + dt.timedelta(days=1)
SEARCH_END = SEARCH_START + relativedelta(months=6)
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
KIWI_API_KEY = os.environ.get('KIWI_API_KEY')


user_manager = UserManager(SHEETY_TOKEN, USERS_URL)
data_manager = DataManager(SHEETY_TOKEN, MY_FLIGHTS_URL)
flight_search = FlightSearch(KIWI_API_KEY)
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

    if flight.price < destination["lowestPrice"] and flight:
        msg = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        # Send me sms
        notification_manager.send_sms(message=msg)

        # Send emails to registered users
        users = user_manager.get_users_data()
        for user in users:
            notification_manager.send_mails(user, msg)

    else:
        print('No good prices.')

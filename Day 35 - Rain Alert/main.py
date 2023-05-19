import datetime as dt
import requests
import smtplib
import os

MY_EMAIL = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('PASSWORD')
YOUR_EMAIL = os.environ.get('YOUR_EMAIL')

city_name = input('Enter city name: ')
now = dt.datetime.now()

WEATHER_PARAMS = {
    'appid': os.environ.get('API_KEY'),
    'units': 'metric',
    'lang': 'pl',
    'limit': 1,
    'exclude': 'minutely,current,daily'
}

# Look for the city coordinates and insert them to weather parameters
geocoding_url = f'http://api.openweathermap.org/geo/1.0/direct?appid={WEATHER_PARAMS["appid"]}&q={city_name}'
geo_response = requests.get(url=geocoding_url)
geo_response.raise_for_status()
WEATHER_PARAMS['lon'] = geo_response.json()[0]['lon']
WEATHER_PARAMS['lat'] = geo_response.json()[0]['lat']

openweathermap_url = 'https://api.openweathermap.org/data/2.8/onecall?'
weather_response = requests.get(url=openweathermap_url, params=WEATHER_PARAMS)
weather_response.raise_for_status()
weather_data_h = weather_response.json()['hourly']

will_rain = False
for hour in weather_data_h[:12]:
    if hour['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP('smtp.mail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg="Subject: It's gonna rain!\n\nPlease take an umbrella with you!")

import requests
import datetime as dt
import smtplib
import time

# Kraków, Poland
MY_LAT = 50.049683
MY_LNG = 19.944544
MY_EMAIL = 'me@mail.com'
MY_PASSWORD = 'password'
SMTP_SERVER = 'smtp.mail.com'

PARAMETERS = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

SUN_URL = 'https://api.sunrise-sunset.org/json'
SATELITE_URL = 'http://api.open-notify.org/iss-now.json'


def is_it_night():
    """Check if in picked location is now nighttime."""

    sun_response = requests.get(url=SUN_URL, params=PARAMETERS)
    sun_response.raise_for_status()

    sun_satelite_data = sun_response.json()
    sunrise_h = int(sun_satelite_data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset_h = int(sun_satelite_data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = dt.datetime.now()

    if time_now.hour not in range(sunrise_h, sunset_h + 1):
        return True
    else:
        return False


def is_satelite_close():
    """Check if satelite is near picked location."""

    satelite_response = requests.get(url=SATELITE_URL)
    satelite_data = satelite_response.json()

    sat_lng = float(satelite_data['iss_position']['longitude'])
    sat_lat = float(satelite_data['iss_position']['latitude'])
        
    if sat_lat - 5 < MY_LAT < sat_lng + 5 and sat_lng - 5 < MY_LNG < sat_lng + 5:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_it_night() and is_satelite_close():
        with smtplib.SMTP(host=SMTP_SERVER) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs='you@gmail.com',
                msg="It's here!")

        break

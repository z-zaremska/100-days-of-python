import os
import requests
import smtplib
from bs4 import BeautifulSoup

TARGET_PRICE = 100
MY_EMAIL = os.environ.get('MY_EMAIL')
MY_EMAIL_PASSWORD = os.environ.get('MY_EMAIL_PASSWORD')
EMAIL_TO_NOTIFY = os.environ.get('EMAIL_TO_NOTIFY')
SMTP_SERVER = os.environ.get('SMTP_SERVER')
URL = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
ACCEPT_LANGUAGE = 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7'

headers = {
    'User-Agent': USER_AGENT,
    'Accept-Language': ACCEPT_LANGUAGE
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()
site_text = response.text

soup = BeautifulSoup(site_text, parser='lxml', features='lxml')
whole_number = soup.find(name='span', class_='a-price-whole').text.split('.')[0]
decimal_number = soup.find(name='span', class_='a-price-fraction').text
current_price = eval(f'{whole_number} + {decimal_number} * 0.01')


if current_price < TARGET_PRICE:
    with smtplib.SMTP_SSL('smtp.poczta.onet.pl:465') as connection:
        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
        message = f"""Subject: SUPER PROMO!
        
        Check this out!
        Your product is cheaper than ever ({current_price})!
        See on the website: {URL}"""

        connection.sendmail(from_addr=MY_EMAIL, to_addrs=EMAIL_TO_NOTIFY, msg=message)
else:
    print(f'Sorry, the price is still high: {current_price}')

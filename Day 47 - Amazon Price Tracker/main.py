import requests
from bs4 import BeautifulSoup

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
whole_number = soup.find(name='span', class_='a-price-whole').contens
decimal_number = soup.find(name='span', class_='a-price-fraction').contents

print(whole_number, decimal_number)

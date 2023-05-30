import requests
from bs4 import BeautifulSoup

requested_date = input("Enter the date you want to move back in time to (yyyy-mm-dd): ")
BILLBOARD_URL = f'https://www.billboard.com/charts/hot-100/{requested_date}/'
playlist_response = requests.get(url=BILLBOARD_URL).text

top_100 = {}

soup = BeautifulSoup(playlist_response, 'html.parser')
top_rows = soup.select('ul.o-chart-results-list-row')

for row in top_rows:
    position = row.select('li.o-chart-results-list__item span')[0].getText().strip()
    author = row.select('li.o-chart-results-list__item span')[1].getText().strip()
    title = row.select('li.lrv-u-width-100p ul li h3')[0].getText().strip()
    top_100[f'{position}'] = {'author': author, 'title': title}

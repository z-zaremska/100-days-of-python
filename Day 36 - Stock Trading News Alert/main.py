import datetime as dt
import requests
import os
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
NEWSAPI_API_KEY = os.environ.get('NEWSAPI_API_KEY')
SMTP_SERVER = os.environ.get('SMTP_SERVER')
MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')
YOUR_EMAIL = os.environ.get('YOUR_EMAIL')
status = None

STOCK_PARAMETERS = {
    'symbol': STOCK,
    'function': 'TIME_SERIES_INTRADAY',
    'interval': '60min',
    'apikey': os.environ.get('ALPHAVANTAGE_API_KEY')
}

NEWS_PARAMETERS = {
    'apiKey': NEWSAPI_API_KEY,
    'q': COMPANY_NAME,
    'searchIn': 'title',
    'language': 'en',
}


def get_stock_data(endpoint: str, parameters: dict):
    """Retrieve hourly stock data."""

    stock_response = requests.get(endpoint, params=parameters)
    stock_response.raise_for_status()

    return stock_response.json()["Time Series (60min)"]


def get_news(endpoint: str, parameters: dict):
    """Retrieve last 3 news about company."""

    news_response = requests.get(endpoint, params=parameters)
    news_response.raise_for_status()
    articles = []

    for news in news_response.json()["articles"][:3]:
        title = news['title']
        description = news['description']
        article = f'Title: {title}\nBrief: {description}\n'
        articles.append(article)

    return articles


def check_difference():
    global status

    yesterday = (dt.date.today() - dt.timedelta(days=2)).strftime("%Y-%m-%d 20:00:00")
    day_before_yesterday = (dt.date.today() - dt.timedelta(days=3)).strftime("%Y-%m-%d 20:00:00")

    stock_1 = float(stock_data[yesterday]['4. close'])
    stock_2 = float(stock_data[day_before_yesterday]['4. close'])
    diff = stock_1/stock_2 - 1

    if diff > 0.05:
        status = 'increased'
    elif diff < -0.05:
        status = 'decreased'

    return diff


stock_data = get_stock_data(STOCK_ENDPOINT, STOCK_PARAMETERS)
change = check_difference()

if status is not None:
    articles = get_news(NEWS_ENDPOINT, NEWS_PARAMETERS)
    print(articles)
    # Send an email with last 3 news about company.
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        if status == 'increased':
            beginning = f'{STOCK}: 🔺 {round(change*100, 0)} %'
        elif status == 'decreased':
            beginning = f'{STOCK}: 🔻 {round(change*100, 0)} %'

        message = f'{beginning}\n\n{articles[0]}\n{articles[1]}\n{articles[2]}'
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=YOUR_EMAIL, msg=message)

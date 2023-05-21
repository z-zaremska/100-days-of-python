import datetime as dt
import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
NEWSAPI_API_KEY = os.environ.get('NEWSAPI_API_KEY')

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

    return news_response.json()["articles"][:3]


def check_difference():
    yesterday = (dt.date.today() - dt.timedelta(days=2)).strftime("%Y-%m-%d 20:00:00")
    day_before_yesterday = (dt.date.today() - dt.timedelta(days=3)).strftime("%Y-%m-%d 20:00:00")

    stock_1 = float(stock_data[yesterday]['5. volume'])
    stock_2 = float(stock_data[day_before_yesterday]['5. volume'])
    diff = stock_1/stock_2 - 1
    print(diff)

    if diff > 0.05:
        return 'increased'
    elif diff < -0.05:
        return 'decreased'
    else:
        return None


stock_data = get_stock_data(STOCK_ENDPOINT, STOCK_PARAMETERS)

status = check_difference()

if status is not None:
    news_data = get_news(NEWS_ENDPOINT, NEWS_PARAMETERS)
    print(news_data)
    if status == 'increased':
        print('Get news - it increased!')
    elif status == 'decreased':
        print('Get news - it decreased!')




## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.






## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

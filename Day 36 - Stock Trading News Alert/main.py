import datetime as dt
import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = os.environ.get('API_KEY')

STOCK_PARAMETERS = {
    'symbol': STOCK,
    'function': 'TIME_SERIES_INTRADAY',
    'interval': '60min',
    'apikey': API_KEY
}

yesterday = (dt.date.today() - dt.timedelta(days=2)).strftime("%Y-%m-%d 20:00:00")
day_before_yesterday = (dt.date.today() - dt.timedelta(days=3)).strftime("%Y-%m-%d 20:00:00")


def check_difference():
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


stock_url = 'https://www.alphavantage.co/query'
stock_response = requests.get(stock_url, params=STOCK_PARAMETERS)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (60min)"]

status = check_difference()

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

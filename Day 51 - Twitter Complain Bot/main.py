import os
import time
from twitterbot import InternetSpeedTwitterBot

PROMISED_UP = 35
PROMISED_DOWN = 350
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')
TWITTER_USERNAME = os.environ.get('TWITTER_USERNAME')
CHROME_DRIVER = os.environ.get('CHROME_DRIVER')

twitter_bot = InternetSpeedTwitterBot(
    up=PROMISED_UP,
    down=PROMISED_DOWN,
    driver_path=CHROME_DRIVER,
    username=TWITTER_USERNAME,
    password=TWITTER_PASSWORD
)

twitter_bot.get_internet_speed()

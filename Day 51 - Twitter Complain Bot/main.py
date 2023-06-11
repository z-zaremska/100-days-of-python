import os
import time
from twitterbot import InternetSpeedTwitterBot

PROMISED_UP = 10
PROMISED_DOWN = 100
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')
TWITTER_USERNAME = os.environ.get('TWITTER_USERNAME')
CHROME_DRIVER = os.environ.get('CHROME_DRIVER')

twitter_bot = InternetSpeedTwitterBot(
    up=PROMISED_UP,
    down=PROMISED_DOWN,
    driver_path=CHROME_DRIVER
)

twitter_bot.log_into_account(
    username=TWITTER_USERNAME,
    password=TWITTER_PASSWORD
)



#
#
# write_tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
# write_tweet = driver.find_element(by=By.XPATH, value=write_tweet_xpath)
#
# message = 'Elo, elo. 520...'
#
# write_tweet.send_keys(message)

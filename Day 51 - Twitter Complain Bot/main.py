import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


PROMISED_UP = 10
PROMISED_DOWN = 100
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')
TWITTER_USERNAME = os.environ.get('MY_EMAIL')
TWITTER_URL = 'https://twitter.com'
SPEEDTEST_URL = 'https://www.speedtest.net/pl'
CHROME_DRIVER = os.environ.get('CHROME_DRIVER')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_service = Service(executable_path=CHROME_DRIVER)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get(url=TWITTER_URL)

# Go to login page
login_page_xpath = '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a'
login_page = driver.find_element(by=By.XPATH, value=login_page_xpath)
login_page.click()

time.sleep(2)

# Log into personal account
enter_username_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
enter_username = driver.find_element(by=By.XPATH, value=enter_username_xpath)
enter_username.send_keys(TWITTER_USERNAME)

next_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
next_button = driver.find_element(by=By.XPATH, value=next_button_xpath)
next_button.click()

time.sleep(2)

enter_password_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
enter_password = driver.find_element(by=By.XPATH, value=enter_password_xpath)
enter_password.send_keys(TWITTER_PASSWORD)

login_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
login_button = driver.find_element(by=By.XPATH, value=login_button_xpath)
login_button.click()

time.sleep(2)

write_tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
write_tweet = driver.find_element(by=By.XPATH, value=write_tweet_xpath)

message = 'Elo, elo. 520...'

write_tweet.send_keys(message)

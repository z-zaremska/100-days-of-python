import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


PROMISED_UP = 10
PROMISED_DOWN = 100
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')
TWITTER_USERNAME = os.environ.get('MY_EMAIL')
TWITTER_URL = 'https://twitter.com'
CHROME_DRIVER = os.environ.get('CHROME_DRIVER')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_service = Service(executable_path=CHROME_DRIVER)
driver = webdriver.Chrome(service=chrome_service)

driver.get(url=TWITTER_URL)

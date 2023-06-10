import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

COOKIE_URL = 'https://orteil.dashnet.org/experiments/cookie/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = os.environ.get('CHROME_DRIVER')
chrome_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get(COOKIE_URL)

# Game panel
cookie_button = driver.find_element(by=By.ID, value='cookie')
rewards_bought = 0

game_start_time = time.time()
timeout = time.time() + 60*5


while time.time() < timeout:
    # Click the cookie.
    cookie_button.click()

    if time.time() > game_start_time + 20:
        # Check rewards current prices
        rewards = driver.find_element(by=By.ID, value='store').find_elements(
            by=By.CSS_SELECTOR, value='div > b')

        # Create rewards dictionary
        rewards_dict = {}
        for reward in rewards[:-1]:
            name, price = reward.text.strip().split('\n')[0].split(' - ')
            rewards_dict[int(price.replace(',', ''))] = name

        # Check current number of cookies
        number_of_cookies = int(driver.find_element(
                                                    by=By.XPATH,
                                                    value='//*[@id="money"]'
                                                ).text.replace(',', ''))
        try:
            max_reward = [name for price, name in sorted(rewards_dict.items()) if price < number_of_cookies][-1]

            buy_reward = driver.find_element(by=By.ID, value=f'buy{max_reward}')
            buy_reward.click()
            game_start_time += 5
            rewards_bought += 1
        except Exception:
            continue

cookies_per_sec = driver.find_element(by=By.ID, value='cps')
driver.close()

print(f'Cookies per second: {cookies_per_sec.text}')
print(f'Bought rewards: {rewards_bought}')

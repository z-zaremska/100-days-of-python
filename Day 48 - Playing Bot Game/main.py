from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = 'https://www.python.org/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = '/Users/zuzaz/Development/chromedriver.exe'
chrome_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get(URL)

events_xpath = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul'
events = driver.find_element(by=By.XPATH, value=events_xpath)

events = events.find_elements(by=By.TAG_NAME, value='li')

events_dict = {}

for index, event in enumerate(events):
    date, event_name = event.text.split('\n')
    events_dict[index] = {
        'time': date,
        'name': event_name
    }

driver.quit()

print(events_dict)

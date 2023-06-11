import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

LINKEDIN_USERNAME = os.environ.get('LINKEDIN_USERNAME')
LINKEDIN_PASSWORD = os.environ.get('LINKEDIN_PASSWORD')
CHROME_DRIVER = os.environ.get('CHROME_DRIVER')
LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3605301781&f_AL=true&f_E=1%2C2&f_WT=2&geoId=105072130&keywords=junior%20python&location=Polska&refresh=true&sortBy=DD"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_service = Service(executable_path=CHROME_DRIVER)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get(LINKEDIN_URL)

# Go to login page
login_page = driver.find_element(
    by=By.CSS_SELECTOR,
    value='body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis'
)
login_page.click()

# Log into an account
enter_username = driver.find_element(by=By.ID, value='username')
enter_username.send_keys(LINKEDIN_USERNAME)
enter_password = driver.find_element(by=By.ID, value='password')
enter_password.send_keys(LINKEDIN_PASSWORD)

login_button = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
login_button.click()

time.sleep(1)

# Hide messenger window
hide_messenger = driver.find_element(by=By.ID, value='ember113')
hide_messenger.click()

# Find job offers
job_offers = driver.find_elements(by=By.CSS_SELECTOR, value='#main > div > div.scaffold-layout__list > div > ul > li')
counter = 0

for job in job_offers:
    job.click()
    job_details = driver.find_element(by=By.CLASS_NAME, value='jobs-unified-top-card__content--two-pane')
    time.sleep(3)

    # Save job offer if job wasn't already saved.
    save_button = job_details.find_element(by=By.CSS_SELECTOR, value='button.jobs-save-button')
    if save_button.text.split('\n')[0].lower() == 'zapisz':
        save_button.click()

# Go to saved jobs
driver.get('https://www.linkedin.com/my-items/saved-jobs/?cardType=SAVED')

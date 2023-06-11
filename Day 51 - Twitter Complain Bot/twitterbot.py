import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class InternetSpeedTwitterBot:
    TWITTER_URL = 'https://twitter.com'
    SPEEDTEST_URL = 'https://www.speedtest.net/pl'

    def __init__(self, up: int, down: int, driver_path: str):
        self.up = up
        self.down = down

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        chrome_service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(
            service=chrome_service,
            options=chrome_options
        )

        self.go_to_site(self.TWITTER_URL)

    def go_to_site(self, site_url: str):
        """Opens the site from given url."""
        self.driver.get(url=site_url)

    def log_into_account(self, username, password):
        """
        Log into personal Twitter account with given username
        and password.
        """

        # Go to login page.
        login_page_xpath = '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a'
        login_page = self.driver.find_element(
            by=By.XPATH,
            value=login_page_xpath
        )
        login_page.click()

        time.sleep(2)

        # Enter username.
        enter_username_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
        enter_username = self.driver.find_element(
            by=By.XPATH,
            value=enter_username_xpath
        )
        enter_username.send_keys(username)

        # Click on "Next" button.
        next_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
        next_button = self.driver.find_element(
            by=By.XPATH,
            value=next_button_xpath
        )
        next_button.click()

        time.sleep(2)

        # Enter password.
        enter_password_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
        enter_password = self.driver.find_element(
            by=By.XPATH,
            value=enter_password_xpath
        )
        enter_password.send_keys(password)

        # Click on "Login" button.
        login_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
        login_button = self.driver.find_element(
            by=By.XPATH,
            value=login_button_xpath
        )
        login_button.click()

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass

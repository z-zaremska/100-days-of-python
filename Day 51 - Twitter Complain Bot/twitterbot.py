from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class InternetSpeedTwitterBot:

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

    def go_to_site(self, site_url: str):
        """Opens the site from given url."""
        self.driver.get(url=site_url)

    def log_into_account(self, username, password):
        pass

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass

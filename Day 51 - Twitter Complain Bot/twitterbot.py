import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class InternetSpeedTwitterBot:
    TWITTER_URL = 'https://twitter.com'
    SPEEDTEST_URL = 'https://www.speedtest.net/pl'

    def __init__(self, up: int, down: int, driver_path: str, username: str, password: str):
        self.up = up
        self.down = down
        self.username = username
        self.password = password

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        chrome_service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(
            service=chrome_service,
            options=chrome_options
        )

    def log_into_account(self, username: str, password: str):
        """
        Log into personal Twitter account with given username
        and password.
        """

        self.driver.get(self.TWITTER_URL)

        # Go to login page.
        login_page_xpath = '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a'
        login_page = self.driver.find_element(
            by=By.XPATH,
            value=login_page_xpath
        )
        login_page.click()

        time.sleep(1)

        # Enter username.
        enter_username_selector = '#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu.r-13qz1uu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input'
        enter_username = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=enter_username_selector
        )
        enter_username.send_keys(username)

        # Click on "Next" button.
        next_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
        next_button = self.driver.find_element(
            by=By.XPATH,
            value=next_button_xpath
        )
        next_button.click()

        time.sleep(1)

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

        time.sleep(2)

    def tweet_at_provider(self, current_down: float, current_up: float):
        """Create and publish tweet about internet provider."""

        activate_tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
        activate_tweet = self.driver.find_element(by=By.XPATH, value=activate_tweet_xpath)
        activate_tweet.click()

        time.sleep(1)

        write_tweet_path = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
        write_tweet = self.driver.find_element(by=By.XPATH, value=write_tweet_path)

        message = f"""Hey, UPC!
My download speed is {current_down} Mb/s and upload speed is {current_up} Mb/s!
And you've promised something else (upload: {self.up}; download: {self.down})!"""

        write_tweet.send_keys(message)

        public_button_spath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]'
        public_button = self.driver.find_element(by=By.XPATH, value=public_button_spath)
        public_button.click()

    def get_internet_speed(self):
        """Check the current internet speed."""

        self.driver.get(self.SPEEDTEST_URL)
        time.sleep(2)

        accept_conditions = self.driver.find_element(by=By.ID,
                                                     value='onetrust-accept-btn-handler')
        accept_conditions.click()

        start_test_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        start_test = self.driver.find_element(
            by=By.XPATH,
            value=start_test_xpath
        )
        start_test.click()

        print('Waiting for speed test to finish...')
        time.sleep(60)
        print('Speed test has finished.')

        notification_dismiss = self.driver.find_element(
            by=By.LINK_TEXT,
            value='Powrót do wyników testu'
        )
        notification_dismiss.click()

        current_up = float(self.driver.find_element(
            by=By.CLASS_NAME,
            value='upload-speed'
        ).text)
        current_down = float(self.driver.find_element(
            by=By.CLASS_NAME,
            value='download-speed'
        ).text)

        print(
            f'Current parameters:\nUpload: {current_up} ({self.up})\nDownload: {current_down} ({self.down})')

        if current_up < self.up or current_down < self.down:
            self.log_into_account(username=self.username, password=self.password)
            self.tweet_at_provider(current_down, current_up)
            print('Too low!')

        else:
            print("Everything's fine")

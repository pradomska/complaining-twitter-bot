from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

MY_EMAIL = "example@gmail.pl"
MY_PASSWORD = "******"
PROMISED_DOWN = 200
PROMISED_UP = 10
CHROME_DRIVE_PATH = "C:/Development/chromedriver.exe"
TWITTER_URL = "https://twitter.com/login"
SPEED_URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(driver_path), options=webdriver.ChromeOptions())
        self.down = 0
        self.up = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_URL)

        accept_button = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        accept_button.click()

        sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()

        sleep(40)

        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)

        sleep(5)

        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(MY_EMAIL)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()

        sleep(5)

        try:
            user_check = self.driver.find_element(By.CSS_SELECTOR, 'div input')
            user_check.send_keys('username')

            sleep(3)

            user_check.send_keys(Keys.ENTER)

            sleep(3)
        except NoSuchElementException:
            print("No veryfi by username or phone number")
            pass

        sleep(3)

        password = self.driver.find_elements(By.CSS_SELECTOR, 'div input')[1]
        password.send_keys(MY_PASSWORD)

        sleep(2)

        password.send_keys(Keys.ENTER)

        sleep(5)

        tweet_compose = self.driver.find_element(By.XPATH,"//div[contains(@aria-label, 'Tweet text')]")

        sleep(5)
        tweet_compose.send_keys(str(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"))

        sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()

        sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVE_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()

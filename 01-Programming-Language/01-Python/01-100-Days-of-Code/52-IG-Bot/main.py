from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

CHROME_DRIVER_PATH = ''
SIMILAR_ACCOUNT = ''
USERNAME = ''
PASSWORD = ''

class InstaFollower:
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(USERNAME)
        self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(PASSWORD)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[3]/button').click()

    def find_followers(self):
        time.sleep(3)
        self.driver.get(SIMILAR_ACCOUNT)


    def follow(self):
        time.sleep(5)
        xpath_pattern = "//button[contains(@class, '_acan') and contains(@class, '_acap') and contains(@class, '_acas') and contains(@class, '_aj1-') and contains(@class, '_ap30')]"

        try:
            all_buttons = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath_pattern))
            )

            for button in all_buttons:
                try:
                    # Scroll the button into view and then click
                    self.driver.execute_script("arguments[0].scrollIntoView();", button)
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button))
                    button.click()
                    time.sleep(4)
                    print("following...")
                except ElementClickInterceptedException:
                    # Handle the click interception
                    cancel_button_xpath = '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]'
                    cancel_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, cancel_button_xpath))
                    )
                    cancel_button.click()
                except TimeoutException:
                    print("Timeout waiting for the button to be clickable")

        except TimeoutException:
            print("Timeout waiting for buttons to be present")

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
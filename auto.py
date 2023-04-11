from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class Krishi():
    url = 'https://www.instagram.com/accounts/login/'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    username = 'aru_high_key'
    password = 'arun8870insta'
    username_locator = 'username'
    password_locator = 'password'
    LoginButtonLocator = '//*[@id="loginForm"]/div/div[3]'

    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def Login(self):
        self.Browsing()
        time.sleep(10)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.LoginButtonLocator).click()
        while(True):
            pass

k = Krishi()

k.Login()

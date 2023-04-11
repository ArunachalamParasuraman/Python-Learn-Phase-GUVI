from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class Selin():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    Username_Locator = 'username'
    Password_Locator = 'password'
    LoginButtonLocator = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    Username = 'Admin'
    Password = 'admin123'

    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
    
    def To_Get_Cookies(self):
        self.Browsing()
        return self.driver.get_cookies()
    
    def Check_Cookies(self):
        self.Browsing()
        sleep(4)
        Before_login = self.driver.get_cookies()[0]['value']
        self.driver.find_element(by=By.NAME, value=self.Username_Locator).send_keys(self.Username)
        self.driver.find_element(by=By.NAME, value=self.Password_Locator).send_keys(self.Password)
        self.driver.find_element(by=By.XPATH, value=self.LoginButtonLocator).click()
        sleep(4)
        After_login = self.driver.get_cookies()[0]['value']
        print('value before login :',Before_login)
        print('value after login :',After_login)
        print()
        if Before_login != After_login:
            print('Login is success')
        else:
            print('Failed')

s = Selin()

print(s.To_Get_Cookies())

s.Check_Cookies()
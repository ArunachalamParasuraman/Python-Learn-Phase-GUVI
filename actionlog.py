from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class Chains():
    url = 'https://opensource-demo.orangehrmlive.com'
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    action = ActionChains(driver)
    Username = 'Admin'
    Password = 'admin123'
    Username_Locator = 'username'
    Password_Locator = 'password'
    LoginButtonLocator = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    DropDownLocator = '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span'
    LogoutLocator = 'Logout'

    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
    
    def Logout(self):
        self.browsing()
        sleep(4)
        self.driver.find_element(by=By.NAME, value=self.Username_Locator).send_keys(self.Username)
        self.driver.find_element(by=By.NAME, value=self.Password_Locator).send_keys(self.Password)
        self.driver.find_element(by=By.XPATH, value=self.LoginButtonLocator).click()
        sleep(4)
        Dropdown = self.driver.find_element(by=By.XPATH, value=self.DropDownLocator)
        self.action.click(on_element=Dropdown).perform()
        sleep(3)
        self.driver.find_element(by=By.LINK_TEXT, value=self.LogoutLocator).click()
        sleep(3)
        self.driver.close()

Chains().Logout()
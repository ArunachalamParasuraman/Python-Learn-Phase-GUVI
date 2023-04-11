from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

class Explicit_use():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    wait = WebDriverWait(driver, 20)
    Username_Locator = 'email'
    Password_Locator = 'pass'
    LoginButtonLocator = 'login'
    username = 'suman@guvi.in'
    password = 'suman@123'

    def __init__(self, url):
        self.url = url
        self.driver.maximize_window()
        self.driver.get(self.url)
    
    def Login(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, self.Username_Locator))).send_keys(self.username)
            self.wait.until(EC.presence_of_element_located((By.ID, self.Password_Locator))).send_keys(self.password)
            self.wait.until(EC.presence_of_element_located((By.NAME, self.LoginButtonLocator))).click()
        except NoSuchElementException:
            print('some elements are missing')
        finally:
            self.driver.quit()
    
    def Login_again(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, self.Username_Locator))).send_keys(self.username)
            self.wait.until(EC.visibility_of_element_located((By.ID, self.Password_Locator))).send_keys(self.password)
            self.wait.until(EC.visibility_of_element_located((By.NAME, self.LoginButtonLocator))).click()
        except StaleElementReferenceException:
            print('element is not visible')
        finally:
            self.driver.quit()
    
    def title_is(self):
        try:
            print(self.driver.title == 'facebook')
        except:
            print(False)
        finally:
            self.driver.quit()
    
    def url_to_be(self, test_url):
        try:
            if(self.driver.current_url == test_url):
                    print(True)
        except:
            print(False)
        finally:
            self.driver.quit()


e = Explicit_use('https://www.facebook.com/')

e.Login()

e.Login_again()

e.title_is()

e.url_to_be('facebook.com')
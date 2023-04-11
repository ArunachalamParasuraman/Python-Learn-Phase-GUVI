from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class Cowin():
    url = 'https://www.cowin.gov.in/'
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    ABHALocator = '/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[1]/a/span'
    DashboardLocator = '/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[2]/a'
    VerifyLocator = '/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[3]/a'
    FAQLocator = '/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a'
    PartnerLocator = '/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a'

    def Window(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(4)
        parent_window = self.driver.current_window_handle
        self.driver.find_element(by=By.XPATH, value=self.ABHALocator).click()
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=self.DashboardLocator).click()
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=self.VerifyLocator).click()
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=self.FAQLocator).click()
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=self.PartnerLocator).click()
        all_window = self.driver.window_handles
        print('unique code for parent tab :',parent_window)
        print('unique code for all tab :',all_window)
        print()
        for unique_tab_code in all_window:
            if unique_tab_code != parent_window:
                self.driver.switch_to.window(unique_tab_code)
                sleep(4)
                self.driver.close()

c = Cowin()

c.Window()
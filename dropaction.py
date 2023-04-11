from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class Action_ch():
    url = 'https://qavbox.github.io/demo/dragndrop/' #https://jqueryui.com/droppable/
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    action = ActionChains(driver)
    source = 'draggable'
    target = 'droppable'

    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
    
    def Drag_Drop(self):
        self.Browsing()
        sleep(5)
        source = self.driver.find_element(by=By.ID, value=self.source)
        target = self.driver.find_element(by=By.ID, value=self.target)
        self.action.drag_and_drop(source,target).perform()
    
    def Drag_Drop_Offset(self):
        self.Browsing()
        sleep(5)
        source = self.driver.find_element(by=By.ID, value=self.source)
        target = self.driver.find_element(by=By.ID, value=self.target)
        self.action.drag_and_drop_by_offset(source, 100, 100).perform()

a = Action_ch()
a.Drag_Drop()
#a.Drag_Drop_Offset()



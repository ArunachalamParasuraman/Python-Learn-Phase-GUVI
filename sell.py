from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
 
class Arun:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
 
    # constructor method class Suman
    def __init__(self, url):
        self.url = url
 
    # fetch the title of the webpage using Python Selenium
    def get_title(self):
        self.driver.get(self.url)
        return self.driver.title
   
    # fetch the URL of the webpage
    def get_url(self):
        self.driver.get(self.url)
        return self.driver.current_url
   
    # fetch the entire content of the webpage
    def get_webpage(self):
        self.driver.maximize_window()
        self.driver.get(self.url)        
        return self.driver.page_source
 
 
s = Arun('https://www.guvi.in')
 
print(s.get_title())
 
#print(s.get_url())
 
#print(s.get_webpage())

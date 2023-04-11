from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from time import sleep
from imlocator import Locators

class IMDB():
    url = 'https://www.imdb.com/search/title/'
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
    
    def Imdb_Filling(self):
        self.Browsing()
        sleep(10)
        User_Min = self.driver.find_element(by=By.NAME, value=Locators().User_RatingMIN)
        User_Min_Dropdown = Select(User_Min)
        User_Min_Dropdown.select_by_visible_text(Locators().User_RatingMIN_Text)
        User_Max = self.driver.find_element(by=By.NAME, value=Locators().User_RatingMAX)
        User_Max_Dropdown = Select(User_Max)
        User_Max_Dropdown.select_by_visible_text(Locators().User_RatingMAX_Text)
        sleep(3)
        Display = self.driver.find_element(by=By.ID, value=Locators().Display_id)
        Display_Per_Page = Select(Display)
        Display_Per_Page.select_by_value(Locators().Display_value)
        sleep(3)
        language = self.driver.find_element(by=By.NAME, value=Locators().Lang_Name)
        language_Select = Select(language)
        language_Select.select_by_index(4)
        sleep(3)
        language_Select.select_by_value(Locators().Lang_Value)
        sleep(3)
        language_Select.select_by_visible_text(Locators().Lang_Text)
        sleep(3)
        language_Select.deselect_by_index(4)
        sleep(3)
        language_Select.deselect_by_value(Locators().Lang_Value)
        sleep(3)
        language_Select.deselect_by_visible_text(Locators().Lang_Text)
        sleep(5)
        language_option = language_Select.options
        for lang in language_option:
            lang.click()
        sleep(10)
        language_Select.deselect_all()


i  = IMDB()

i.Imdb_Filling()
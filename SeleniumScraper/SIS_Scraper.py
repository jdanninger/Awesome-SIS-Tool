import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SIS_Scraper:
    driver = None # webdriver
    term = None # String
    searchMe = None # String list
    search = None

    def __init__(self, term, searchTerm):
        os.environ['PATH'] += r"/Users/jdanninger/Documents/GitHub/Awesome-SIS-Tool/SeleniumScraper/chromedriver"
        self.term = term
        self.searchMe = searchTerm
        self.driver = webdriver.Chrome()


    def __str__(self):
        return str ("Search term: " + self.searchMe + " for term " + self.term)

    def setupSearch(self):
        self.driver.get("https://sisguest.case.edu/")
        self.driver.implicitly_wait(10)
        class_search = self.driver.find_element(By.ID, "win0groupletPTNUI_LAND_REC_GROUPLET$0")
        class_search.click()
        self.driver.implicitly_wait(10)
        fall_23 = self.driver.find_element(By.XPATH, "//*[text()='" + self.term + "']")
        self.driver.implicitly_wait(10)
        fall_23.click()
        self.driver.implicitly_wait(10)
        search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        self.driver.implicitly_wait(10)
        search.click()
        self.driver.implicitly_wait(10)
        return search

    def search(self):
        # if self.search == None :
        search = self.setupSearch()
        search.send_keys(self.searchMe)
        search.send_keys(Keys.RETURN)
        self.getListObj()


    def getListObj(self):
        WebDriverWait(self.driver, 20).until(

        )
        test = self.driver.find_element(By.ID, "win3divDESCR100$grid$0")
        test.find_element(By.TAG_NAME, "Strong")
        print(test)
        while True:
            pass






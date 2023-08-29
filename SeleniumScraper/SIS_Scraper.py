import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class SIS_Scraper:
    driver = None # webdriver
    term = None # String
    searchMe = None # String list
    search = None

    def __init__(self, term, searchTerm):
        os.environ['PATH'] += r"/Users/jdanninger/Documents/GitHub/Awesome-SIS-Tool/SeleniumScraper/chromedriver"
        self.term = term
        self.searchMe = searchTerm
        options = webdriver.ChromeOptions()
        dump = "/Users/jdanninger/Documents/GitHub/Awesome-SIS-Tool/SeleniumScraper/Excel Dump"
        options.add_experimental_option( "prefs", { "download.default_directory": dump })
        self.driver = webdriver.Chrome(options=options)


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
        search = self.setupSearch()
        search.send_keys(self.searchMe)
        search.send_keys(Keys.RETURN)
        self.downloadExcel()


    def downloadExcel(self):
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element(
                (By.ID, "processing")
            )
        )
        self.driver.find_element(By.ID, "CW_CLSRCH_WRK2_TC_EXCEL_BTN").click()
        while True:
            pass









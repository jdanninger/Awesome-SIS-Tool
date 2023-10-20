import os
import time

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SISScraper:
    def __init__(self):
        os.environ['PATH'] += r"chromedriver"

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_experimental_option( "prefs", { "download.default_directory": os.getcwd() })
        self.driver = webdriver.Chrome(options=options)
        
    def search(self, semester, search_term):
        self.driver.get("https://sisguest.case.edu/psc/P92SCWR_7/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&1&scname=CS_SSR_MANAGE_CLASSES_NAV&ICAJAXTrf=true")
        self.driver.implicitly_wait(10)
        
        fall_23 = self.driver.find_element(By.XPATH, "//*[text()='" + semester + "']")
        self.waitUntilProcesingDone()
        fall_23.click()
        self.driver.implicitly_wait(10)
        
        search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        self.waitUntilProcesingDone()
        search.click()
        self.driver.implicitly_wait(10)

        search.send_keys(search_term)
        search.send_keys(Keys.RETURN)
        self.downloadExcel()

    def waitUntilProcesingDone(self):
        WebDriverWait(self.driver, 60).until(
            EC.invisibility_of_element(
                (By.ID, "processing")
            )
        )

    def downloadExcel(self):
        self.waitUntilProcesingDone()
        self.driver.find_element(By.ID, "CW_CLSRCH_WRK2_TC_EXCEL_BTN").click()
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element((By.ID, "processing")))
        time.sleep(2)
import os
import time

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class SISScraper:
    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()

        if headless:
            options.add_argument("--headless")
            
        options.add_experimental_option( "prefs", { "download.default_directory": os.getcwd() })
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    def search(self, semester, search_term):
        print("Opening SIS")

        self.driver.get("https://sisguest.case.edu/psc/P92SCWR_7/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&1&scname=CS_SSR_MANAGE_CLASSES_NAV&ICAJAXTrf=true")
        self.driver.implicitly_wait(10)

        print(f"Finding {semester}")

        semester_bttn = self.driver.find_element(By.XPATH, "//*[text()='" + semester + "']")
        self.waitUntilProcesingDone()
        semester_bttn.click()
        self.driver.implicitly_wait(10)
        
        search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        self.waitUntilProcesingDone()
        search.click()
        self.driver.implicitly_wait(10)

        print(f"Searching for {search_term}")
        search.send_keys(search_term)
        search.send_keys(Keys.RETURN)
        self.downloadExcel()

        print("Finished")

    def waitUntilProcesingDone(self):
        WebDriverWait(self.driver, 60).until(
            EC.invisibility_of_element(
                (By.ID, "processing")
            )
        )

    def downloadExcel(self):
        print(f"Downloading the excel file")

        self.waitUntilProcesingDone()
        self.driver.find_element(By.ID, "CW_CLSRCH_WRK2_TC_EXCEL_BTN").click()
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element((By.ID, "processing")))
        time.sleep(2)
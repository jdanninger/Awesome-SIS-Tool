import os
import time

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from excel_reader import ExcelReader

class SISScraper:
    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()

        if headless: options.add_argument("--headless")
        options.add_experimental_option( "prefs", { "download.default_directory": os.getcwd() })
        
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )        

    def search_term(self, course): 
        return " ".join(str(course[field]) for field in ["course_code", "course_name"] if course[field] is not None)

    def check_courses(self, courses):
        # Open SIS in the browser
        print("Opening SIS")

        self.driver.get("https://sisguest.case.edu/psc/P92SCWR_7/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&1&scname=CS_SSR_MANAGE_CLASSES_NAV&ICAJAXTrf=true")
        self.driver.implicitly_wait(10)

        # Click on the Spring 2024 semester
        print(f"Finding the semester")

        semester_bttn = self.driver.find_element(By.XPATH, "//*[text()='Spring 2024']")
        self.wait_to_process()
        semester_bttn.click()
        self.driver.implicitly_wait(10)

        # Check the availability of each coures
        availability = []

        for i, course in enumerate(courses):
            search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
            self.wait_to_process()
            search.click()
            search.clear()
            
            self.driver.implicitly_wait(10)

            print(f"Searching for the course")

            search.send_keys(self.search_term(course))
            search.send_keys(Keys.RETURN)
            
            self.download_excel()

            reader = ExcelReader()

            is_available = reader.is_available(course)
            availability.append(is_available)

            print(f"{i+1} / {len(courses)} courses checked")

        return availability

    def wait_to_process(self):
        WebDriverWait(self.driver, 60).until(
            EC.invisibility_of_element(
                (By.ID, "processing")
            )
        )

    def download_excel(self):
        print(f"Downloading the excel file")

        self.wait_to_process()
        self.driver.find_element(By.ID, "CW_CLSRCH_WRK2_TC_EXCEL_BTN").click()
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element((By.ID, "processing")))
        time.sleep(2)
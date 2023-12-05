import sys
sys.path.append('..')

import unittest
from sis_scraper import SISScraper

class TestSISScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = SISScraper(headless=False)

    # def test_headless(self):
    #     scraper = SISScraper(headless=True)

    def test_check_courses(self):
        course = {
            "code": "CSDS",
            "number": "132",
            "name": "Programming in Java",
            "section": None,
            "days": None,
            "time": None,
            "prof": None
        }

        self.scraper.check_courses([course])

    # def test_search_term(self):
    #     course = {
    #         "code": "CSDS",
    #         "number": "132",
    #         "name": "Intro to Programming in Java"
    #     }

    #     course2 = {
    #         "code": None,
    #         "number": None,
    #         "name": "Calculus 1"
    #     }

    #     print(self.scraper.search_term(course))
    #     print(self.scraper.search_term(course2))

if __name__ == "__main__":
    unittest.main()
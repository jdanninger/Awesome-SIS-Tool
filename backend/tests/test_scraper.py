import sys
sys.path.append('..')

import unittest
from sis_scraper import SISScraper

class TestSISScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = SISScraper(headless=False)

    def test_headless(self):
        scraper = SISScraper(headless=True)

    def test_search(self):
        # self.scraper.search("Fall 2023", "CSDS 132")
        self.scraper.check_courses()

    def test_search_term(self):
        course = {
            "code": "CSDS",
            "number": "132"
        }

        course2 = {
            "name": "Calculus 1"
        }

        print(self.scraper.search_term(course))
        print(self.scraper.search_term(course2))

if __name__ == "__main__":
    unittest.main()
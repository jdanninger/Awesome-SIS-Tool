import sys
sys.path.append('..')

import unittest
from src.sis_scraper import SISScraper

class TestSISScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = SISScraper(headless=False)

    def test_headless(self):
        scraper = SISScraper(headless=True)

    def test_search(self):
        self.scraper.search("Fall 2023", "CSDS 132")

if __name__ == "__main__":
    unittest.main()
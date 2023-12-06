import sys
sys.path.append('..')

import unittest
from sis_scraper import SISScraper

class TestSISScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = SISScraper(headless=False)

    def test_headless(self):
        scraper = SISScraper(headless=True)

    def test_check_courses(self):
        course = {
            "course_code": "CSDS",
            "course_number": "132",
            "course_id": 1,
            "course_name": "Programming in Java",
            "days": None,
            "professor": None,
            "section": None,
            "time": None,
            "user_name": None
        }

        course2 = {
            "course_code": "MATH",
            "course_number": "121",
            "course_id": 2,
            "course_name": None,
            "days": None,
            "professor": None,
            "section": None,
            "time": None,
            "user_name": None
        }

        self.scraper.check_courses([course, course2])

    def test_search_term(self):
        course = {
            "code": "CSDS",
            "number": "132",
            "name": "Intro to Programming in Java"
        }

        course2 = {
            "code": None,
            "number": None,
            "name": "Calculus 1"
        }

        print(self.scraper.search_term(course))
        print(self.scraper.search_term(course2))

if __name__ == "__main__":
    unittest.main()
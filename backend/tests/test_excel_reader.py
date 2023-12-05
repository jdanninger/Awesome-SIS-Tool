import sys
sys.path.append('..')

import unittest
from excel_reader import ExcelReader

class TestExcelReader(unittest.TestCase):
    def setUp(self):
        self.reader = ExcelReader()

    def test_is_available(self):
        self.reader.is_available()

if __name__ == "__main__":
    unittest.main()
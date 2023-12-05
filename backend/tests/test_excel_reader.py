import sys
sys.path.append('..')

import unittest
from excel_reader import ExcelReader

class TestExcelReader(unittest.TestCase):
    def setUp(self):
        self.reader = ExcelReader()

if __name__ == "__main__":
    unittest.main()
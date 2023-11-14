import pandas as pd
import os

class ExcelReader:

    def __init__(self):
        files = os.listdir(os.getcwd())
        excel_file = None

        for file_name in files:
            if "Output_CW_GUEST" in file_name and ".xlsx" in file_name:
                excel_file = file_name
                break

        self.filename = excel_file

    def is_available(self):
        return True
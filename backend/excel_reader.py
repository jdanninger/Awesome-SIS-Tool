import pandas as pd
import os

class ExcelReader:
    excelDataframe = None
    name = None

    def __init__ (self):
        pass

    def isAvailable(self):
        files = os.listdir(os.getcwd())
        excel_file = None

        for file_name in files:
            if "Output_CW_GUEST" in file_name and ".xlsx" in file_name:
                excel_file = file_name
                break

        if excel_file is None:
            return
            
        
        

import pandas as pd
import os

class Excel_Reader:
    excelDataframe = None
    name = None
    def __init__(self):
        self.__init__("")
    def __init__(self, name):
        self.name = name
        fileName = os.listdir("/Users/jdanninger/Documents/GitHub/Awesome-SIS-Tool/SeleniumScraper/Excel Dump")[0]
        print(pd.read_excel("/Users/jdanninger/Documents/GitHub/Awesome-SIS-Tool/SeleniumScraper/Excel Dump/"+fileName,"1"))
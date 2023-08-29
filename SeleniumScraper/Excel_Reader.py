import pandas as pd

class Excel_Reader:
    excelDataframe = None
    name = None
    def __init__(self):
        self.__init__("")
    def __init__(self, name):
        self.name = name
        exc
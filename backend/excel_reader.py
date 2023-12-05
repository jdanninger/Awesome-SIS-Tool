import pandas as pd
import os

class ExcelReader:

    def __init__(self):
        files = os.listdir(os.getcwd())

        excel_file = ""

        for f in files:
            if "Output_CW_GUEST" in f and ".xlsx" in f:
                excel_file = f
                break
        
        self.filename = str(excel_file)

        # course dict keys mapped to the downloaded csv column names
        self.csv_headers = {
            "code": "SUBJECT",
            "number": "CATALOG_NBR",
            "name": "CW_CLASS_TITLE",
            "section": "CLASS_SECTION",
            "days": "CLASS_MTG_DAYS",
            "time": "CW_CLASS_MTG_TIMES",
            "prof": "INSTR_NAME"
        }

    def is_available(self, course):
        print(self.filename)
        print(type(self.filename))
        df = pd.read_excel(self.filename)

        mask = pd.Series(False, index=df.index)

        for key in course.keys():
            if course[key] is not None:
                if key == "name":
                    mask |= (course[key] in df[self.csv_headers[key]])
                else:
                    mask |= (course[key] == df[self.csv_headers[key]])

        df = df[mask]
        
        # # List to store matching entries
        # matching_entries = []

        # # Loop through all rows
        # for index, row in df.iterrows():
        #     if "Open" in str(row['HELLO']).lower():
        #         matching_entries.append(row)

        # # Create a new DataFrame from the matching entries
        # filtered_df = pd.DataFrame(matching_entries)

        # print(filtered_df)

        return True

    def delete_csv(self):
        pass
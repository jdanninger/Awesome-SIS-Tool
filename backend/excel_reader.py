import pandas as pd
import os

class ExcelReader:

    def __init__(self):
        files = os.listdir(os.getcwd())
        excel_file = None

        for f in files:
            print(f)

            if "Output_CW_GUEST" in f and ".xlsx" in f:
                excel_file = f
                break

        self.filename = excel_file
        print(self.filename)

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
        df = pd.read_csv(self.filename)

        mask = pd.Series(False, index=df.index)

        for key in course.keys():
            if course[key] is not None:
                if key == "name":
                    mask |= (course[key] in df[self.csv_headers[key]])
                else:
                    mask |= (course[key] == df[self.csv_headers[key]])

        filtered_df = df[mask]
        
        print(filtered_df)

        return True

    def delete_csv(self):
        pass
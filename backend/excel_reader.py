import pandas as pd
import os

class ExcelReader:
    def get_csv_path(self):
        files = os.listdir(os.getcwd())

        excel_file = ""

        for f in files:
            if "Output_CW_GUEST" in f and ".xlsx" in f:
                excel_file = f
                break
        
        return excel_file

    def is_available(self, course):     
        csv_path = self.get_csv_path()

        df = pd.read_excel(csv_path)
        os.remove(csv_path)

        mask = pd.Series(False, index=df.index)

        # course dict keys mapped to the downloaded csv column names
        self.csv_headers = {
            "course_code": "SUBJECT",
            "course_num": "CATALOG_NBR",
            "course_name": "CW_CLASS_TITLE",
            "section": "CLASS_SECTION",
            "days": "CLASS_MTG_DAYS",
            "time": "CW_CLASS_MTG_TIMES",
            "professor": "INSTR_NAME"
        }

        for key in course.keys():
            if course[key] is not None:
                if key == "course_id" or key == "user_name":
                    continue

                if key != "name" or key != "professor":
                    mask |= (course[key] == df[self.csv_headers[key]])

        df = df[mask]
        df = df[df["INSTR_NAME"].apply(lambda x: str(x).lower()) == course["professor"].lower()]
        df = df[df["CW_CLASS_TITLE"].apply(lambda x: str(x).lower()) == course["course_name"].lower()]

        for _, row in df.iterrows():
            if "Open" in str(row["ENRL_STATUS"]):
                return "OPEN"

        return "CLOSED"
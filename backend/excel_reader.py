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

        filter = pd.Series(False, index=df.index)

        if course["course_code"]:
            filter = filter | (df["SUBJECT"] == course["course_code"])

        if course["course_num"]:
            filter = filter & (df["CATALOG_NBR"] == int(course["course_num"]))

        if course["course_name"]:
            filter = filter & df["CW_CLASS_TITLE"].apply(lambda x: str(x).lower()).str.contains(course["course_name"].lower())

        if course["section"]:
            filter = filter & (df["CLASS_SECTION"] == int(course["section"]))

        if course["days"]:
            filter = filter & (df["CLASS_MTG_DAYS"].str.strip() == course["days"].strip())

        if course["time"]:
            filter = filter & (df["CW_CLASS_MTG_TIMES"] == course["time"])

        if course["professor"]:
            filter = filter & df["INSTR_NAME"].apply(lambda x: str(x).lower()).str.contains(course["professor"].lower())

        df = df[filter]
        print(df)

        for _, row in df.iterrows():
            if "Open" in str(row["ENRL_STATUS"]):
                return "OPEN"

        return "CLOSED"
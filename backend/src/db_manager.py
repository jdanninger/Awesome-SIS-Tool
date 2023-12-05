from sqlalchemy import create_engine, text

class DBManager:
    def __init__(self):
        url = "postgresql://swe_project_user:Hm9jhHzZa5WDHOWQbDTPIiGHHLNScvb3@dpg-cln4iqkjtl8s7397h5n0-a.ohio-postgres.render.com/swe_project"

        self.engine = create_engine(url)
        self.connection = self.engine.connect()

db = DBManager()
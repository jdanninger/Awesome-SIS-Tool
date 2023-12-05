from sqlalchemy import create_engine, text

class DBManager:
    def __init__(self):
        url = "postgresql://swe_project_user:Hm9jhHzZa5WDHOWQbDTPIiGHHLNScvb3@dpg-cln4iqkjtl8s7397h5n0-a.ohio-postgres.render.com/swe_project"

        engine = create_engine(db_url)
        connection = engine.connect()

        print(connection)

        # Example SELECT query on the 'courseinfo' table
        query = text("SELECT * FROM courseinfo")
        result = connection.execute(query)

        print(result)

        # Fetch all rows from the result set
        rows = result.fetchall()

        # Print the result
        for row in rows:
        print(row)

        # Close the connection
        connection.close()
from flask import Flask, jsonify, request
from sqlalchemy import text

from db_manager import db

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello, World!'

@app.route("/api/signup", methods=["POST"])
def test_endpoint():
    username = request.json.get("username")
    password = request.json.get("password")

    # Make sure username doesn't already exist
    query = text("SELECT * FROM courseinfo WHERE username =: username")
    result = connection.execute(query, username=username)

    rows = result.fetchall()

    if len(rows) > 0:
        return jsonify(message="FAIL")

    # Insert credentials into the users table
    insert_query = text(
        """
        INSERT INTO your_table_name (column1, column2, ...)
        VALUES (:value1, :value2, ...);
        """
    )

    try:
        db.connection.execute(insert_query, **data)

    except Exception as e:
        print(f"Error inserting data: {e}")
        return jsonify(message="ERROR")

    return jsonify(message="SUCCESS")

@app.route("/api/login", methods=["GET"])
def test_endpoint():
    username = request.json.get("username")
    password = request.json.get("password")

    query = text("SELECT * FROM courseinfo WHERE username =: username AND password =: password")
    result = connection.execute(query, username=username, password=password)

    rows = result.fetchall()

    if len(rows) == 1:
        return jsonify(message="SUCCESS")

    return jsonify(message="FAIL")

if __name__ == "__main__":
    app.run(debug=True)
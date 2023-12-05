from flask import Flask, jsonify, request
from sqlalchemy import text

from db_manager import db

app = Flask(__name__)

def insert_data(query):
    try:
        db.connection.execute(query, **data)

    except Exception as e:
        print(f"Error inserting data: {e}")
        return False

    return True

@app.route("/api/signup", methods=["POST"])
def signup():
    username = request.json.get("username")
    password = request.json.get("password")

    # Make sure username doesn't already exist
    query = text("SELECT * FROM courseinfo WHERE username =: username")
    result = connection.execute(query, username=username)

    rows = result.fetchall()

    if len(rows) > 0:
        return jsonify(message="FAIL")

    # Insert credentials into the users table
    query = text(
        """
        INSERT INTO your_table_name (column1, column2, ...)
        VALUES (:value1, :value2, ...);
        """
    )

    if insert_data(query):
        return jsonify(message="SUCCESS")

    return jsonify(message="ERROR")

@app.route("/api/login", methods=["GET"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    query = text("SELECT * FROM courseinfo WHERE username =: username AND password =: password")
    result = connection.execute(query, username=username, password=password)

    rows = result.fetchall()

    if len(rows) == 1:
        return jsonify(message="SUCCESS")

    return jsonify(message="FAIL")

@app.route("/api/add-course", methods=["GET"])
def add_course():

    username = request.json.get("username")
    code = request.json.get("code")
    number = request.json.get("number")
    name = request.json.get("name")
    section = request.json.get("section")
    days = request.json.get("days")
    time = request.json.get("time")
    prof = request.json.get("prof")

    # Insert credentials into the users table
    query = text(
        """
        INSERT INTO your_table_name (column1, column2, ...)
        VALUES (:value1, :value2, ...);
        """
    )

    if insert_data(query):
        return jsonify(message="SUCCESS")

    return jsonify(message="ERROR")

if __name__ == "__main__":
    app.run(debug=True)
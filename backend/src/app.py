from flask import Flask, jsonify, request
from sqlalchemy import text

from db_manager import db
from sis_scraper import SISScraper

app = Flask(__name__)

def insert_data(query, data):
    try:
        db.connection.execute(query, data)
        db.connection.commit()

    except Exception as e:
        print(f"Error inserting data: {e}")
        db.connection.rollback()

        return False

    return True

@app.route("/api/signup", methods=["POST"])
def signup():
    username = request.json.get("username")
    password = request.json.get("password")
    email = request.json.get("email")

    # Make sure username doesn't already exist
    query = text("SELECT * FROM login WHERE username = :username")
    query = query.bindparams(username=username)

    result = db.connection.execute(query, {'username': username})

    rows = result.fetchone()

    if rows is not None: # Fail if the username exists
        return jsonify(message="FAIL")

    # Insert credentials into the users table
    query = text(
        """
        INSERT INTO login (username, password, email)
        VALUES (:username, :password, :email);
        """
    )

    data = {"username": username, "password": password, "email": email}

    if insert_data(query, data):
        return jsonify(message="SUCCESS")

    return jsonify(message="FAIL")

@app.route("/api/login", methods=["GET"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    query = text("SELECT * FROM courseinfo WHERE username = :username AND password = :password")
    result = connection.execute(query, username=username, password=password)

    rows = result.fetchall()

    if len(rows) == 1:
        return jsonify(message="SUCCESS")

    return jsonify(message="FAIL")

@app.route("/api/add-course", methods=["POST"])
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

@app.route("/api/delete-course", methods=["DELETE"])
def delete_course():
    pass

@app.route("/api/get-tracked-courses", methods=["GET"])
def get_tracked_courses():
    username = request.json.get("username")

    query = text("SELECT * FROM courseinfo WHERE username =: username")
    result = connection.execute(query, username=username, password=password)

    rows = result.fetchall()
    
    # Check if no courses are tracked
    if len(rows) == 0:
        return jsonify({})
    
    # Get all tracked courses
    courses = []

    for row in rows:
        courses.append(row)

    return jsonify(courses)

@app.route("/api/start-tracking", methods=["GET"])
def start_tracking():
    scraper = SISScraper()

if __name__ == "__main__":
    app.run(debug=True)
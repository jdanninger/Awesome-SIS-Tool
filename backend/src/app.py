from flask import Flask, jsonify, request
from db_manager import db

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello, World!'

@app.route("/api/create-new-user", methods=["POST"])
def test_endpoint():
    username = request.json.get("username")
    password = request.json.get("password")

    print(username)
    print(password)

    return jsonify(message="SUCCESS")

    # insert_query = text(
    #     """
    #     INSERT INTO your_table_name (column1, column2, ...)
    #     VALUES (:value1, :value2, ...);
    #     """
    # )

    # try:
    #     self.connection.execute(insert_query, **data)
    #     return jsonify(message="SUCCESS")

    # except Exception as e:
    #     print(f"Error inserting data: {e}")
    #     return jsonify(message="ERROR")

if __name__ == '__main__':
    app.run(debug=True)
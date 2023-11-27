
from flask import Flask, render_template
import pymysql

db = pymysql.connect(host="localhost", user="root", password="Neha0315!", database="case-coursewatch")

app = Flask(__name__)

@app.route("/")
def someName():
    cursor = db.cursor()
    sql = "SELECT * FROM TABLE"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("index.html", results=results)
 
if __name__ == "__main__":
    app.run(debug=True)
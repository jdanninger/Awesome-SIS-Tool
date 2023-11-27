
from flask import Flask, render_template
import pymysql



#app = Flask(__name__)

#@app.route("/")
#def someName():
   
    #return render_template("index.html", results=results)
 
if __name__ == "__main__":
   # app.run(debug=True)
    db = pymysql.connect(host="localhost", user="root", password="Neha0315!", database="case-coursewatch")
    cursor = db.cursor()
    sql = "SELECT * FROM `case-coursewatch`.CourseInfo;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)

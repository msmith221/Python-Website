from flask import Flask
from flask import render_template
from flask import url_for
from flask import request, flash

import sqlite3 as sql

from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    return '<html><body><h1>Hello World</h1></body></html>'

@app.route('/welcome')
def welcome_page():
    return render_template('welcome.html')

@app.route('/index')
def index_page():
    return render_template("index.html")

#@app.route('/login',methods = ['POST', 'GET'])
#def login():
#    if request.method == 'POST':
#        user = request.form['nm']
#        return redirect(url_for('success',name = user))
#    else:
#            user = request.args.get('nm')
#            return redirect(url_for('success',name = user))

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/greetings/')
def greetings_page():
    return 'Enter a holiday into your URL to see some seasonal greetings! EX: http://localhost:5000/greetings/christmas'

@app.route('/greetings/<name>')
def greetings_type(name):
    if name == 'christmas':
        return 'Merry Christmas!'
    if name == 'newyear':
        return 'Happy New Year!'
    if name == 'easter':
        return 'Happy Easter!'
    if name == 'birthday':
        return 'Your birthday isnt a holiday, but ill allow it. HAPPY BIRTHDAY!'

@app.route('/list')
def list_data():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall();
    return render_template("list.html", rows = rows)

@app.route('/myform')
def new_student():
    return render_template('student.html')

@app.route('/addrec',methods = ["POST"])
def addrec():
    if request.method == "POST":
        nm = request.form["nm"]
        addr = request.form["add"]
        city = request.form["cty"]
        pin = request.form["pin"]

        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name, address, city, pin) VALUES (?,?,?,?)", [nm, addr, city, pin])
        con.commit()

        return render_template("list.html")


#def create_database():
 #   conn = sql.connect("database.db")
  #  conn.execute("CREATE TABLE students (name TEXT, address TEXT, city TEXT, pin TEXT)")
   # conn.close()

#create_database()

#conn = sql.connect('database.db')
#print("Opened database successfully!");

#conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
#print("Table created successfully");
#conn.close()

@app.route("/boot")
def boot_demo():
    return render_template("boot.html")

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, session
import sqlite3 as sql

app = Flask(__name__,template_folder='templates',static_folder='statics')

@app.route("/")
def index():
    return render_template('flask_app/index.html')

@app.route("/about")
def about():
    return render_template('flask_app/team.html')

@app.route("/signup")
def signup():
    return render_template('flask_app/signup.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         email = request.form['email']
         passw = request.form['password']

         
         with sql.connect("user.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (email,password) VALUES (?,?)",(email,passw) )
            con.commit()
            msg = "<h1>Record successfully added!<h1>"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("flask_app/index.html",msg = msg)
         con.close()
@app.route("/login")
def login():
    return render_template('flask_app/login.html')

if __name__==("__main__"):
    app.run(debug=True)

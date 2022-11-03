from flask import Flask,render_template

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

@app.route("/login")
def login():
    return render_template('flask_app/login.html')

if __name__==("__main__"):
    app.run()
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
user = {}
usr= "asd"

@app.route('/', methods=['GET', 'POST'])
def home():
    login_page = True
    print(request.values.get('page'))
    if request.values.get('page') == "register":
        login_page = False
    return render_template('index.html', login=login_page)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global usr
    global user
    if request.method == "POST":
        if user[request.form["email"]] == request.form['password']:
            i=request.form["email"]
            print(i,type(i))
            usr = i[0:-10]
            return redirect(url_for('tracker'))
        else:
            return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        mail_id = request.form['email']
        passw = request.form['password']
        user[mail_id] = passw
        print(user)
        return redirect(url_for('home', page="login"))


@app.route('/tracker')
def tracker():
    global usr
    return render_template('home.html',usr= usr )


@app.route('/add-expenditure', methods=['GET', 'POST'])
def add_expenditure():
    if request.method == "POST":
        details = request.form
        print(details)
        return redirect(url_for('tracker'))


if __name__ == '__main__':
    app.run(debug=True)

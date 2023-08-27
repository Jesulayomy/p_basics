#!/usr/bin/env python3
from flask import Flask, session
from flask import redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required


app = Flask(__name__)
app.secret_key = b'256438e0bbcb880cf8eb2e61ed4955728aa018cccfdf3d398d87b2439c7d9a58'
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/maths', methods=['GET'])
def maths():
    return f'Two plus two is four'

@app.route('/books', methods=['GET'])
def books():
    if "username" not in session:
        return redirect(url_for('login'))
    return f'Books are great {session["username"]}'

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

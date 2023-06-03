from flask import Flask, request, render_template, redirect, url_for

import sqlite3
from flask_login import UserMixin, login_manager, login_user, login_required, logout_user, current_user
app = Flask(__name__)

@app.route('/baza', methods=['GET', 'POST'])
def index():

    conn = sqlite3.connect("workers.db")
    c = conn.cursor()

    c.execute("SELECT * FROM workers")
    data = c.fetchall()

    conn.close()

    html = "<h1>RFID Card Data</h1>"
    html += "<table><tr><th>Imie</th><th>Nazwisko</th><th>ID</th><th>Sala</th></tr>"
    for row in data:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>"
    html += "</table>"

    return html

@app.route('/login', methods=['GET', 'POST'])
def admin():
    conn = sqlite3.connect("workers.db")
    c = conn.cursor()

    c.execute("SELECT * FROM workers")
    data = c.fetchall()

    conn.close()

    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        # Check if login and password are correct
        if login == 'admin' and password == 'haslo':
            # If credentials are correct, redirect to another page
            return redirect('/admin')
        else:
            # If credentials are incorrect, render the login page again with an error message
            error = 'Invalid login or password'
            return render_template('login.html', error=error)

        # Render the login page for GET requests
    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    return "Witaj admin!"

@app.before_request
def require_admin():
    # Check if the user is authenticated
    if not is_authenticated():
        # If not authenticated, redirect to the login page
        return redirect(url_for('login'))
def is_authenticated():
    # Check if the user is authenticated
    # Implement your authentication logic here
    # For demonstration purposes, return a hardcoded value
    return True  # Change this logic to suit your requirements

if __name__ == '__main__':
    app.run(debug=True, port=8080)


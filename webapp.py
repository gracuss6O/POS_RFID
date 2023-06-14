from flask import Flask, request, render_template, redirect, url_for, jsonify, session

import sqlite3

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/', methods=['GET', 'POST'])
def base():
    return render_template('base.html')

@app.route('/logi', methods=['GET', 'POST'])
def index():

    conn = sqlite3.connect("logi.db")# zmiana na logi
    c = conn.cursor()

    c.execute("SELECT * FROM logi")
    data = c.fetchall()
    conn.close()

    html = "<h1>Spis użytkowników przykładających kartę RFID do czytników.</h1>"
    html += "<table><tr><th>Imie</th><th>Nazwisko</th><th>ID</th><th>Sala</th><th>Data godzina</th></tr>"
    for row in data:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>"
    html += "</table>"

    return html

@app.route('/login', methods=['GET', 'POST'])
def login():

    """czyszczenie calej bazy logi, zastanowic sie czy potrzebne i czy umiescic gdzies indziej
    conn = sqlite3.connect("logi.db")
    c = conn.cursor()

    c.execute('DELETE FROM logi;', );

    conn.commit()
    conn.close()
    """


    conn = sqlite3.connect("workers.db")
    c = conn.cursor()

    c.execute("SELECT * FROM workers")
    data = c.fetchall()

    conn.close()

    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        ##if login == 'admin' and password == 'haslo':
        if request.form['login'] == 'admin' and request.form['password'] == 'haslo':
            session['admin'] = request.form['login']

            return redirect('/admin')
        else:
            error = 'Invalid login or password'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    ##require_admin()

   ## if request.method == 'POST':
    if 'admin' not in session:
        return redirect(url_for('login'))
    else:
        imie= request.form.get('imie')
        nazwisko = request.form.get('nazwisko')
        idcard = request.form.get('idcard')
        sala = request.form.get('sala')
        action = request.form.get('action')


        if action == 'add':
            conn = sqlite3.connect('workers.db')
            c = conn.cursor()
            c.execute("INSERT INTO workers (imie, nazwisko, idcard, sala) VALUES (?, ?, ?, ?)",
                      (imie, nazwisko, idcard, sala))
            conn.commit()
            conn.close()
        elif action == 'update':
            conn = sqlite3.connect('workers.db')
            c = conn.cursor()
            c.execute("UPDATE workers SET imie = ?, nazwisko = ?, idcard = ?, sala = ? WHERE idcard = ?",
                      (imie, nazwisko, idcard, sala, idcard))
            conn.commit()
            conn.close()
        elif action == 'delete':
            conn = sqlite3.connect('workers.db')
            c = conn.cursor()
            c.execute("DELETE FROM workers WHERE imie = ? AND nazwisko = ? AND idcard = ? AND sala = ?",
                           (imie, nazwisko, idcard, sala))

            conn.commit()
            conn.close()
    conn = sqlite3.connect('workers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM workers")
    records = c.fetchall()
    conn.close()

    return render_template('adminpage.html', records=records)
##nowe zmiany, w logach widoczne tylko wpisy z desktopapp

@app.before_request
def require_admin():

    if not is_authenticated():
        return redirect(url_for('login'))
def is_authenticated():

    return True

if __name__ == '__main__':
    app.run(debug=True, port=8080)


from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():

    conn = sqlite3.connect("workers.db")
    c = conn.cursor()

    c.execute("SELECT * FROM workers")
    data = c.fetchall()

    conn.close()

    html = "<h1>RFID Card Data</h1>"
    html += "<table><tr><th>ID</th><th>Class</th></tr>"
    for row in data:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td></tr>"
    html += "</table>"

    return html


if __name__ == '__main__':
    app.run(debug=True, port=8080)


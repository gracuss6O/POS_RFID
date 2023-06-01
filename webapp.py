from flask import Flask, request, render_template

app = Flask(__name__)
strings = []  # Store the received strings

@app.route('/receive_string', methods=['POST'])
def receive_string():
    received_string = request.form.get('string')
    strings.append(received_string)  # Store the received string
    return 'String received successfully'

@app.route('/')
def index():
    return render_template('index.html', strings=strings)  # Pass the stored strings to the template


if __name__ == '__main__':
    app.run()


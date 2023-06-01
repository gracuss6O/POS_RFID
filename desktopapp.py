import tkinter as tk
import requests
def send_string_to_web_app(string):
    url = 'http://localhost:5000/receive_string'  # Adjust the URL to match your Flask application's route
    data = {'string': string}
    response = requests.post(url, data=data)
    print(response.text)  # Print the response from the Flask application
def send_string():
    string = entry.get()  # Assuming you have an entry widget to get the string
    send_string_to_web_app(string)

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Send", command=send_string)
button.pack()
root.mainloop()

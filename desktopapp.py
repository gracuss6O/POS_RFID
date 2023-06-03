import tkinter as tk
import requests
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import *

conn = sqlite3.connect("workers.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS workers
             (idcard TEXT, sala TEXT)''')

conn.commit()
conn.close()

def send_string_to_web_app(idcard, sala):
    url = 'http://localhost:8080'
    data = {
        'idcard': idcard,
        'sala': sala,
            }
    response = requests.post(url, data=data)
    print(response.text)  

def pierwszyprzycisk():

    def send_string():

        idcard = entryid.get()
        sala = entrysala.get()
        send_string_to_web_app(idcard, sala)

        conn = sqlite3.connect("workers.db")
        c = conn.cursor()
        c.execute("INSERT INTO workers (idcard, sala) VALUES (?, ?)", (idcard, sala))
        conn.commit()
        conn.close()

        idcard.delete(0, tk.END)
        sala.delete(0, tk.END)


    top = Toplevel()
    top.title("wprowdzanie danych")
    top.geometry("640x480")


    myLabel = Label(top, text=" Wprowadz dane swojej karty ")
    myLabel.pack()
    labelid=Label(top, text="ID: (format=XXXXYY, gdzie X- litera, Y-cyfra) ")
    labelid.pack()
    entryid = tk.Entry(top)
    entryid.pack()
    labelsala = Label(top, text="sala: ")
    labelsala.pack()
    entrysala = tk.Entry(top)
    entrysala.pack()



    przycisk=tk.Button(top, text="wyslij", command=send_string)
    przycisk.pack()

#pierwsza strona aplikacji
root = tk.Tk()
root.title("Czytnik RFID")
root.geometry("640x480")

#przycisk symulujacy przylozenie RFID
button = tk.Button(root, text="Przyloz", command=pierwszyprzycisk)
button.pack()
button.place(x=270, y=200)

root.mainloop()
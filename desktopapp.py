import tkinter as tk
import requests
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import *

conn = sqlite3.connect("workers.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS workers
             (imie TEXT, nazwisko TEXT, idcard TEXT, sala TEXT)''')

conn.commit()
conn.close()

def send_string_to_web_app(imie, nazwisko, idcard, sala):
    url = 'http://localhost:8080'
    data = {
        'imie':imie,
        'nazwisko':nazwisko,
        'idcard': idcard,
        'sala': sala,
            }
    response = requests.post(url, data=data)
    print(response.text)

def pierwszyprzycisk():

    def send_string():
        imie =entryimie.get()
        nazwisko =entrynazwisko.get()
        idcard = entryid.get()
        sala = entrysala.get()
        send_string_to_web_app(imie, nazwisko,idcard, sala)

        conn = sqlite3.connect("workers.db")
        c = conn.cursor()
        c.execute("INSERT INTO workers (imie, nazwisko, idcard, sala) VALUES (?, ?, ?, ?)", (imie, nazwisko, idcard, sala))
        conn.commit()
        conn.close()


        entryimie.delete(0, tk.END)
        entrynazwisko.delete(0, tk.END)
        entryid.delete(0, tk.END)
        entrysala.delete(0, tk.END)


    top = Toplevel()
    top.title("Wprowdzanie danych")
    top.geometry("640x480")


    myLabel = Label(top, text=" Wprowadz dane.")
    myLabel.pack()
    #imie
    labelimie = Label(top, text="Imie:")
    labelimie.pack()
    entryimie = tk.Entry(top)
    entryimie.pack()
    #nazwisko
    labelnazwisko = Label(top, text="Nazwisko:")
    labelnazwisko.pack()
    entrynazwisko = tk.Entry(top)
    entrynazwisko.pack()
    #id karty
    labelid=Label(top, text="ID:")
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
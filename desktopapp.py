import tkinter as tk
import requests
import sqlite3
from tkinter import *
from datetime import datetime

conn = sqlite3.connect("workers.db")## to bdzie baza admina
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS workers
             (imie TEXT, nazwisko TEXT, idcard TEXT, sala TEXT)''')

conn.commit()
conn.close()
##baza na logi
conn = sqlite3.connect("logi.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS logi
             (imie TEXT, nazwisko TEXT, idcard TEXT, sala TEXT,date DATETIME)''') ## dopisany typ SQL DATETIME

conn.commit()
conn.close()
def send_string_to_web_app(imie, nazwisko, idcard, sala, date): ##data porownac z lementami w bazie
    url = 'http://localhost:8080'
    data = {
        'imie':imie,
        'nazwisko':nazwisko,
        'idcard': idcard,
        'sala': sala,
        'date':date,
            }
    response = requests.post(url, data=data)
    print(response.text)

def pierwszyprzycisk():

    def send_string():
        imie =entryimie.get()
        nazwisko =entrynazwisko.get()
        idcard = entryid.get()
        sala = entrysala.get()
        date =datetime.now()
        send_string_to_web_app(imie, nazwisko,idcard, sala,date) ##dopisano date

        conn = sqlite3.connect("logi.db") ##zamiana workers.db na logi
        c = conn.cursor() ##linijka nizej dopisane date
        c.execute("INSERT INTO logi (imie, nazwisko, idcard, sala, date) VALUES (?, ?, ?, ?, ?)", (imie, nazwisko, idcard, sala,date))
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
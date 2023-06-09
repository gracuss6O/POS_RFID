import tkinter as tk
import requests
import sqlite3
from tkinter import *
from datetime import datetime
import json

conn = sqlite3.connect("workers.db")## to bedzie baza admina
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
#baza do porownywania
conn = sqlite3.connect("compare.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS compare
             (imie TEXT, nazwisko TEXT, idcard TEXT, sala TEXT)''')

conn.commit()
conn.close()
def send_string_to_web_app(imie, nazwisko, idcard, sala, date): ##data porownac z elementami w bazie
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



        conn = sqlite3.connect("compare.db")
        c = conn.cursor()
        c.execute("INSERT INTO compare (imie, nazwisko, idcard, sala) VALUES (?, ?, ?, ?)",
                  (imie, nazwisko, idcard, sala))
        conn.commit()
        conn.close()

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

    def drugiprzycisk():
        spraw = Toplevel()
        spraw.title("Sprawdzenie danych")
        spraw.geometry("640x480")
        Labelspr = Label(spraw, text=" Sprawdzenie danych")
        Labelspr.pack()


        # Connect to the first database
        conn1 = sqlite3.connect(r'C:\Users\Eryk\Documents\GitHub\POS_RFID\compare.db')
        c1 = conn1.cursor()

        # Connect to the second database
        conn2 = sqlite3.connect(r'C:\Users\Eryk\Documents\GitHub\POS_RFID\workers.db')
        c2 = conn2.cursor()

        q1 = "SELECT idcard, sala FROM compare"
        c1.execute(q1)
        records1 = c1.fetchall()

        q2 = "SELECT idcard, sala FROM workers"
        c2.execute(q2)
        records2 = c2.fetchall()

       #sprawdzanie czy sa takie same rekordy w bazach
        found = False
        for record1 in records1:
            if record1 in records2:
                found = True
                break

        if found:
            labeltak = Label(spraw, text=" TAK, masz dostęp ")
            labeltak.pack()

        else:
            labelnie = Label(spraw, text=" NIE, nie masz dostępu")
            labelnie.pack()


        conn1.close()
        conn2.close()

        conn = sqlite3.connect("compare.db")
        c = conn.cursor()

        c.execute('DELETE FROM compare;', );

        conn.commit()
        conn.close()

    przycisk=tk.Button(top, text="Wprowdz dane", command=send_string)
    przycisk.pack()
    przycisksprawdzajacy=tk.Button(top, text="Sprawdz dostep", command=drugiprzycisk)
    przycisksprawdzajacy.pack()


#pierwsza strona aplikacji
root = tk.Tk()
root.title("Czytnik RFID")
root.geometry("640x480")

#przycisk symulujacy przylozenie RFID
button = tk.Button(root, text="Przyloz", command=pierwszyprzycisk)
button.pack()
button.place(x=270, y=200)

root.mainloop()
from tkinter import *
import sqlite3
from webapp import Flask, render_template, request

root = Tk()
root.title("siemanko")
root.geometry("640x480")

con = sqlite3.connect('ludzie.db')

cur = con.cursor()

'''
c.execute("create table addresses (
		first_name text,
		last_name text,
		address text,
		city text,
		state text,
		zipcode integer
		)")
'''



def pierwszyprzycisk():

    top = Toplevel()
    top.title("drugie okon")
    top.geometry("640x480")

    myLabel = Label(top, text=" Wprowadz dane swojej karty ")

    con = sqlite3.connect('ludzie.db')

    cur = con.cursor()

    f_name = Entry(top)
    f_name.place(bordermode=OUTSIDE, height=20, width=100, x=100, y=300)
    f_surname = Entry(top)
    f_surname.place(bordermode=OUTSIDE, height=20, width=100, x=300, y=300)
    f_id = Entry(top)
    f_id.place(bordermode=OUTSIDE, height=20, width=100, x=500, y=300)
    f_name.pack()
    f_surname.pack()
    f_id.pack()

    con.commit()

    con.close()


    def submit():

        con = sqlite3.connect('ludzie.db')

        cur = con.cursor()

        cur.execute("INSERT INTO addresses VALUES (:f_name, :f_surname, :f_id)",)
        {
            'f_name': f_name.get(),
            'f_surname':f_surname.get(),
            'f_id':f_id.get()
        }


        con.commit()

        con.close()



    def query():
        con = sqlite3.connect('ludzie.db')

        cur = con.cursor()

        cur.execute("SELECT * FROM addresses")
        records= cur.fetchall()
        print(records)

        con.commit()

        con.close()

    B = Button(top, text="Potwierdz dane", command=query)


    labelimie = Label(top, text="Imie: ")
    labelnazwisko = Label(top, text="Nazwisko: ")
    labelid = Label(top, text="ID card: ")

    #imie = Text(top)
    #nazwisko = Text(top)
    #id = Text(top)
    myLabel.pack()
    labelimie.pack()
    labelnazwisko.pack()
    labelid.pack()
    B.pack()
    #imie.pack()
    #nazwisko.pack()
    #id.pack()

    labelimie.place(bordermode=OUTSIDE, height=20, width=100, x=100, y=250)
    labelnazwisko.place(bordermode=OUTSIDE, height=20, width=100, x=300, y=250)
    labelid.place(bordermode=OUTSIDE, height=20, width=100, x=500, y=250)
    B.place(x=270, y=400)
    #imie.place(bordermode=OUTSIDE, height=20, width=100, x=100, y=300)
    #nazwisko.place(bordermode=OUTSIDE, height=20, width=100, x=300, y=300)
    #id.place(bordermode=OUTSIDE, height=20, width=100, x=500, y=300)


RFID = Button(root, text="Przyloz swoja karte", command=pierwszyprzycisk)
RFID.pack()
RFID.place(x=270, y=200)

con.commit()

con.close()

root.mainloop()
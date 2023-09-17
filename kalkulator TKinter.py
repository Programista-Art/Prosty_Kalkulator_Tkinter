#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Programista
#
# Created:     17.09.2023
# Copyright:   (c) Programista 2023
# Licence:     <GNU>
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
#+
def btn_oblicz():
    try:
        a = float(liczbaA.get())
        b = float(liczbaB.get())
        c = a + b
        rezultat.config(text=f'Wynik: {c}')
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawne liczby!")
#-
def btn_minus():
    try:
        a = float(liczbaA.get())
        b = float(liczbaB.get())
        c = a - b
        rezultat.config(text=f'Wynik: {c}')
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawne liczby!")

#*
def btn_mnozyc():
    try:
        a = float(liczbaA.get())
        b = float(liczbaB.get())
        c = a * b
        rezultat.config(text=f'Wynik: {c}')
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawne liczby!")

#/
def btn_dzielic():
    try:
        a = float(liczbaA.get())
        b = float(liczbaB.get())
        c = a / b
        rezultat.config(text=f'Wynik: {c}')
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawne liczby!")
root = Tk()
root.title("Kalkulator")
root.geometry("235x160")
root.resizable(width=False, height=False)

frame = Frame(root, bg='#0075db')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# Tworzenie dodatkowego Frame do przycisków operacji
operation_frame = Frame(frame, bg='#0075db')
operation_frame.grid(row=2, column=0, columnspan=4, pady=10)

# Pole A
labelA = Label(frame, text="Liczba A:", bg='#75bfff', font=('Helvetica', 12))
labelA.grid(row=0, column=0, padx=10, pady=5)
liczbaA = Entry(frame, bg='#dbeeff')
liczbaA.grid(row=0, column=1, padx=10, pady=5)

# Pole B
labelB = Label(frame, text="Liczba B:", bg='#75bfff', font=('Helvetica', 12))
labelB.grid(row=1, column=0, padx=10, pady=5)
liczbaB = Entry(frame, bg='#dbeeff')
liczbaB.grid(row=1, column=1, padx=10, pady=5)

# +
btn = Button(operation_frame, text='+', bg='#ffb575', font=('Helvetica', 12), command=btn_oblicz)
btn.pack(side=LEFT, padx=10)

# -
btnMinus = Button(operation_frame, text='-', bg='#ffb575', font=('Helvetica', 12), command=btn_minus)
btnMinus.pack(side=LEFT, padx=10)

# *
btnMnozyc = Button(operation_frame, text='*', bg='#ffb575', font=('Helvetica', 12), command=btn_mnozyc)
btnMnozyc.pack(side=LEFT, padx=10)

# /
btnDzielic = Button(operation_frame, text='/', bg='#ffb575', font=('Helvetica', 12), command=btn_dzielic)
btnDzielic.pack(side=LEFT, padx=10)

rezultat = Label(frame, text='Wynik', bg='#75edff', font=('Helvetica', 12))
rezultat.grid(row=3, columnspan=2, pady=5)


root.mainloop()



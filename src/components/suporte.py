import time
import random
import datetime

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import functools

def JanSuporte():
        
    jansuporte = Tk()
    jansuporte.title("Suporte Bot Mercado Envios")
    jansuporte.geometry("1000x500")
    jansuporte.configure(background="#2b2b2b")
    jansuporte.resizable(width=False, height=False)
    jansuporte.iconbitmap(default="C:\programas\Programaçâo\GitHub\Bot-ML\Bot-ML\images\LogoIcon.ico")

    logo = PhotoImage(file="C:\programas\Programaçâo\GitHub\Bot-ML\Bot-ML\images\logo.png")

    LeftFrame = Frame(jansuporte, width=220, height=500, bg="#FF8C00", relief="raise")
    LeftFrame.pack(side=LEFT)

    RightFrame = Frame(jansuporte, width=775, height=500, bg="#4f4f4f", relief="raise")
    RightFrame.pack(side=RIGHT)

    Valores = Label(RightFrame, text="Suporte por E-mail: ", font=("Century Gothic", 20), bg="#4f4f4f", fg="Black")
    Valores.place(x=5, y=75)

    ValoresEntry = Text(RightFrame, width=40, height=1)
    # ValoresEntry.config(state=state)
    ValoresEntry.place(x=260, y=90)

    ConfButton = ttk.Button(RightFrame, text="Solicitar Suporte por E-mail", width= 30, command=JanSuporte)
    ConfButton.place(x=5, y=150)

    ConfButton = ttk.Button(RightFrame, text="Suporte por Ligação", width= 30, command=JanSuporte)
    ConfButton.place(x=5, y=200)

    ConfButton = ttk.Button(RightFrame, text="Suporte por mensagem", width= 30, command=JanSuporte)
    ConfButton.place(x=5, y=250)

    jansuporte.mainloop()
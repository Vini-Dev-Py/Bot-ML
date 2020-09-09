from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import functools

jan = Tk()
jan.title("Bot Mercado Envios")
jan.geometry("800x300")
jan.configure(background="#2b2b2b")
jan.resizable(width=False, height=False)
jan.iconbitmap(default="C:\programas\Programaçâo\GitHub\Bot-ML\Bot-ML\images\LogoIcon.ico")

logo = PhotoImage(file="C:\programas\Programaçâo\GitHub\Bot-ML\Bot-ML\images\logo.png")

messagebox.showinfo("Hello World !", "Seja Bem-Vindo ")

LeftFrame = Frame(jan, width=220, height=500, bg="#FF8C00", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=575, height=500, bg="#4f4f4f", relief="raise")
RightFrame.pack(side=RIGHT)

Caixas = Label(RightFrame, text="Total De Caixas:", font=("Century Gothic", 20), bg="#4f4f4f", fg="Black")
Caixas.place(x=5, y=10)

CaixasEntry = ttk.Entry(RightFrame, width=53)
CaixasEntry.place(x=230, y=25)

Lote = Label(RightFrame, text="Nº Do Lote:", font=("Century Gothic", 20), bg="#4f4f4f", fg="Black")
Lote.place(x=5, y=75)

LoteEntry = ttk.Entry(RightFrame, width=53)
LoteEntry.place(x=230, y=90)

Valores = Label(RightFrame, text="Codigos Lidos: ", font=("Century Gothic", 20), bg="#4f4f4f", fg="Black")
Valores.place(x=5, y=140)

ValoresEntry = Text(RightFrame, width=40, height=5)
# ValoresEntry.config(state=state)
ValoresEntry.place(x=230, y=155)

def lote():
    Lote = LoteEntry.get()

    print(Lote)

ConfButton = ttk.Button(RightFrame, text="Adicionar Lista", width= 30, command=lote)
ConfButton.place(x=5, y=190)

jan.mainloop()
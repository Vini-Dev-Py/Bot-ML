from tkinter import messagebox

from funcconflista import FuncConferir

class Bot:
    def __init__(self, Lista):
        self.Lista = Lista

    def conferirLista(self, Lista):

        self.Lista = Lista

        l = [

        ]

        cont = 0

        ContMenosUm = 0

        def ConferirBarCode(valor):

            quant = len(valor)

            return quant

        FuncConferir(Lista, ContMenosUm, ConferirBarCode, l, cont)
                
        l.sort()

        self.Lista = l
        
        conf = True
        
        return self.Lista

import datetime

from tkinter import messagebox

date = datetime.date.today()

class Salvar:
    def __init__(self, File, date, Lista):
        self.File = File
        self.date = date
        self.Lista = Lista

    def SalvarTxT(self, File, Lista, date):

        self.File = File
        self.Lista = Lista
        self.date = date

        L1 = [
            
        ]

        try:
            File = open(f'C:\programas\Programaçâo\GitHub\{date} QR-BarCode-Unity.txt', 'w+')

            try:
                for i in Lista:
                    File.write(i)
                File.close
            except:
                messagebox.showerror("Erro !", f"Não Foi Possivel Escrever No Arquivo {date} QR-BarCode-Unity.txt")

        except:
            messagebox.showerror("Erro !", "Não Foi Possivel Criar esse Arquivo")

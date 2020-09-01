from tkinter import messagebox

def FuncConferir(Lista, ContMenosUm, ConferirBarCode, l, cont):
    for i in Lista:
            valor = i.strip()

            if valor == -1 or valor == '-1':

                ContMenosUm += 1
            
            else:

                QuantDeDig  = ConferirBarCode(valor)

                if QuantDeDig == 122 or QuantDeDig == 40:
                    
                    if valor not in l:

                        print("oi")

                        l.append(valor)

                    else:

                        cont += 1

                        if cont != 0:

                            messagebox.showerror("Erro !", f"Encontramos {cont} Problemas Na Sua Lista De Codigos")

                        elif cont == 0:

                            messagebox.showinfo(title="Incrivel !", message="Nosso Sistema não achou nem uma falha em sua lista de Codigos, continue assim")

                else:

                    if QuantDeDig > 122 or QuantDeDig > 40:
                        #Terminar
                        messagebox.showerror("Erro !", f"Seu Codigo {valor} tem menos de 11 Digitos")

                    elif QuantDeDig < 122 or QuantDeDig < 40:
                        #Terminar
                        messagebox.showerror("Erro !", f"Seu Codigo {valor} tem mais de 11 Digitos")
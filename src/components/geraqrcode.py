import pyqrcode as pqr
import png
import io

import string
import random

from geraPDF import GeraPdf

L_nomes = [

]

def id_generator(Lista, size=8, chars=string.ascii_uppercase + string.digits):

    for value in Lista:
        nome = ''.join(random.choice(chars) for _ in range(size))

        L_nomes.append(nome)

    print("Hello World")
    print(L_nomes)

def Gerar(Lista, contador):
    for valor in Lista:

        id_generator(Lista)

        contador += 1

        code = pqr.create(valor)

        #for AddNomes in L_nomes:

        with open(f'C:\programas\Programaçâo\GitHub\qrcode\{L_nomes[contador]}.png', 'w'):
            code.png(f'C:\programas\Programaçâo\GitHub\qrcode\{L_nomes[contador]}.png', scale=10)

        code.png(f'C:\programas\Programaçâo\GitHub\qrcode\{L_nomes[contador]}.png', scale=10)

        # buffer = io.BytesIO()

        # code.png(buffer)

    GeraPdf(Lista, L_nomes)

    print("Hello !")
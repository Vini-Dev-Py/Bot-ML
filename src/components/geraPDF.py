from fpdf import FPDF

import datetime

data_Hoje = datetime.date.today()

def GeraPdf(Lista, L_nomes):

    pos_nome = 1

    cont_pos = 5

    cont_alt = 10

    cont = 0

    cont_linhas = 0

    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 13.0)
    pdf.cell(ln=0, h=12.0, align='L', w=0, txt=f"{data_Hoje}", border=0)

    for img in Lista:

        print(L_nomes)

        print(pos_nome)

        nome = L_nomes[pos_nome]

        print(nome)

        pdf.image(f'C:\programas\Programaçâo\GitHub\qrcode\{nome}.png', cont_pos, cont_alt, 40)

        cont += 1
        cont_linhas += 1
        pos_nome += 1

        if cont_linhas == 5:

            cont_pos = 5

            cont_alt += 40

            cont_linhas = 0

        else:
            cont_pos += 40

    pdf.output(f'code.pdf', 'F')
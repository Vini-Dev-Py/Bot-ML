from fpdf import FPDF

import datetime

data_Hoje = datetime.date.today()

def GeraPdf(Lista, L_nomes, contador):

    cont_pos = 5

    cont_alt = 10

    cont = 0

    cont_linhas = 0

    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 13.0)
    pdf.cell(ln=0, h=12.0, align='L', w=0, txt=f"{data_Hoje}", border=0) #{L_nomes[contador]}

    for img in Lista:

        pdf.image(f'C:\programas\Programaçâo\GitHub\qrcode/{L_nomes[contador]}.png', cont_pos, cont_alt, 40)
        cont += 1
        cont_linhas += 1

        if cont_linhas == 5:

            cont_pos = 5

            cont_alt += 40

        else:
            cont_pos += 40

    pdf.output(f'code.pdf', 'F')
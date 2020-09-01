from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_xy(0, 0)
pdf.set_font('arial', 'B', 13.0)
pdf.cell(ln=0, h=12.0, align='L', w=0, txt="Hello World", border=0)
pdf.image('C:\programas\Programaçâo\GitHub\qrcode\HOLOYY4W.png', 10, 58, 40)
pdf.image('C:\programas\Programaçâo\GitHub\qrcode\HOLOYY4W.png', 50, 8, 33)
# pdf.image('C:\programas\Programaçâo\GitHub\qrcode\HOLOYY4W.png', 75, 8, 33)
# pdf.image('C:\programas\Programaçâo\GitHub\qrcode\HOLOYY4W.png', 110, 8, 33)
# pdf.image('C:\programas\Programaçâo\GitHub\qrcode\HOLOYY4W.png', 145, 8, 33)
pdf.output('t.pdf', 'F')
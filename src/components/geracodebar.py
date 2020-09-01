import barcode

from barcode.writer import ImageWriter

barcode = barcode.get_barcode_class('code39')

Hr = barcode('40081414204', writer=ImageWriter())

print(type(Hr))
print(Hr)

bar = Hr.save("C:\programas\Programaçâo\GitHub\code")

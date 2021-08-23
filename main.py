import qrcode

with open ("nazwy.txt", "r") as file:
    nazwy = file.read().splitlines()

with open ("linki.txt", "r") as file:
    linki = file.read().splitlines()

for i in range(len(nazwy)):
    img = qrcode.make(linki[i])
    img.save("tu_gotowe_zdjecia/" + nazwy[i] + ".jpg")
with open("bla.txt") as soubor:
    obsah = soubor.read()
    print(obsah)


# cteni souboru po radcich
with open("bla.txt") as soubor:
    for radek in soubor.readlines():
        if len(radek) > 20:
            print(radek.upper())
        else:
            print(radek)


with open("novy.txt", "w") as soubor:
    soubor.write("Tohle je prvni zapis do souboru \n")
    soubor.write("testsjidosjofj")

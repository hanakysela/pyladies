def nacti_cislo():
    odpoved = int(input("Zadej cislo:"))

    try:
        cislo = int(odpoved)
    except ValueError:
        print("To neni cislo")
    else:
        print("vyjimka nenastala")
    finally:
        print("tohle je kod, ktery se spusti, at je nebo neni chyba")
nacti_cislo()

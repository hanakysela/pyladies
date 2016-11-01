from random import randint

def vyhodnot(abcd):
        if "xxx" in abcd:
                vysledek = "x"
        elif "ooo" in abcd:
                vysledek = "o"
        elif "-" not in abcd and "xxx" not in abcd and "ooo" not in abcd:
                vysledek = "!"
        else: vysledek = "-"
        print(vysledek)
        return

def tah(pole, cislo_policka, symbol):
    return (pole[:cislo_policka-1] + symbol + pole[cislo_policka:])

pole = ("-------------")

### tah_pc
def tah_pc(cislo_policka):
    cislo_policka = randint(0,20)
    while (pole[cislo_policka-1]) != "-":
        cislo_policka = randint(0,20)
    return tah(pole, cislo_policka, "o")


###tah hrace###
def tah_hrace():
    cislo_policka=int(input("Zadej cislo: "))
    while cislo_policka > 20:
        if cislo_policka > 20:
            print("To je moc nebo malo")
        cislo_policka = int(input("Zadej cislo policka:"))
    return tah(pole, cislo_policka, "x")


print(pole)
print(tah_pc())

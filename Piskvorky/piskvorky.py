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


###tah hrace###
print(pole)
cislo_policka=int(input("Zadej cislo: "))
while cislo_policka > 20 or cislo_policka < 1 or pole[cislo_policka-1] != "-":
    if cislo_policka > 20:
        print("To je moc nebo malo")
    elif cislo_policka<1:
        print("To je malo")
    elif pole[cislo_policka-1] != "-":
        print("Tady uz neco je")
    #elif cislo_policka == 0:
        #cislo_policka = int(input("Zadej cislo policka 3:"))
    cislo_policka = int(input("Zadej cislo policka:"))
pole = tah(pole, cislo_policka, "x")
print(pole)
vyhodnot(pole)

###tah PC###
cislo_policka=randint(0,20)
while (pole[cislo_policka-1]) != "-":
    cislo_policka = randint(0,20)
pole = tah(pole, cislo_policka, "o")
print(pole)
vyhodnot(pole)
#print("asi nekdo vyhral")

from random import randint


PC = randint(1,20)
#print(PC)
uzivatel=(int(input("Zadej cislo:")))

#Vyhodnot

tip = 0

while (PC != uzivatel and tip<6):
    print(" jeste ti zbyva", 6-tip, "pokusu")
    if uzivatel < PC:
        print("myslim vetsi")
    elif uzivatel > PC:
        print("myslim mensi")
    tip = tip+1
    uzivatel=(int(input("Zadej cislo:")))
if tip == 6:
    print("mels 6 pokusu a nestacilo to?")

if PC == uzivatel:
        print("vyhral jsi")

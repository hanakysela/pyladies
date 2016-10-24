from random import randrange

clovek = input("Zadej kamen, nuzky, nebo papir pro sebe:")

PC_los = randrange(3)

if PC_los == 0:
    PC  = "kamen"
elif PC_los == 1:
    PC = "nuzky"
else:
    PC = "papir"

if clovek == PC:
    print("Plichta")
elif (clovek == "nuzky" and PC == "papir") or (clovek == "papir" and PC == "kamen") or (clovek == "kamen" and PC == "nuzky"):
    print("Clovek vyhral")
else:
    print("Vyhral PC")

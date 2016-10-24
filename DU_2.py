from random import randrange

clovek = input("Zadej kamen, nuzky, nebo papir pro sebe:")

PC_los = randrange(2)

if PC_los == 0:
    PC  = "kamen"
elif PC_los == 1:
    PC = "nuzky"
else:
    PC = "papir"


if PC == "kamen":
    if clovek == "kamen":
        print("dva kameny, plichta")
    elif clovek == "papir":
        print("vyhral clovek")
    elif clovek == "nuzky":
        print("vyhral PC")
    else:
        print("Clovek si vybral nepripustnou zbran :( ")

elif PC == "nuzky":
    if clovek == "nuzky":
        print("dvoje nuzky, plichta")
    elif clovek == "kamen":
        print("vyhral clovek")
    elif clovek == "papir":
        print("vyhral PC")
    else:
        print("Clovek si vybral nepripustnou zbran :( ")

elif PC == "papir":
    if clovek == "papir":
        print("dva papiry, plichta")
    elif clovek == "nuzky":
        print("vyhral clovek")
    elif clovek == "kamen":
        print("vyhral PC")
    else:
        print("Clovek si vybral nepripustnou zbran :( ")

PC = input("Zadej kamen, nuzky, nebo papir pro PC:")
clovek = input("Zadej kamen, nuzky, nebo papir pro sebe:")

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

else:
    print("PC si vybral nepripustnou zbran :( ")

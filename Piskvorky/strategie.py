from random import randint


def vyhodnot(pole):
    if 'xxx' in pole:
        return 'x'
    elif 'ooo' in pole:
        return 'o'
    elif '-' not in pole:  # Nikdy nepouzivejte not '-' in pole, je to mene citelne
        return '!'
    else:
        return '-'


def tah(pole, index, symbol):  # Ukazka DRY principu, vytahli jsme spolecny kod do jedne funkce
    """Vrati herni pole s danym symbolem umistnym na danou pozici."""
    return pole[:index] + symbol + pole[index + 1:]


def tah_hrace(pole):
    """Ziska od uzivatele pozici, kam chce tahnout, a vrati pole se zaznamenanym tahem hrace."""
    while True:
        pozice = input('Kam chces hrat? (0..{})'.format(len(pole) - 1))
        if pozice.isdigit():  # Staci opravdu isdigit?
            pozice = int(pozice)
            if pozice < 0 or pozice >= len(pole):
                print('Nemuzes hrat venku z pole!')
            elif pole[pozice] != '-':
                print('Tam neni volno!')
            else:
                return tah(pole, pozice, 'o')
        else:
            print('To neni cislo!')


def tah_pocitace(pole):
    """Vrati herni pole se zaznamenaným tahem pocitace."""
    from random import randint
    pozice = -1

    ## vitezne tahy
    if ("x-x") in pole:
        pozice = (pole.index("x-x")) + 1
    elif("-xx") in pole:
        pozice = (pole.index("-xx"))
    elif("xx-") in pole:
        pozice = (pole.index("xx-")) + 2

    ## zabraneni vyhre cloveka na posledni okamzik
    elif ("o-o") in pole:
        pozice = (pole.index("o-o")) + 1
    elif("-oo") in pole:
        pozice = (pole.index("-oo"))
    elif("oo-") in pole:
        pozice = (pole.index("oo-")) + 2

    ##nenechej soupere dychat I
    elif ("--o-") in pole:
        pozice = (pole.index("--o")) + 1
    elif ("-o--") in pole:
        pozice = (pole.index("o--")) + 2

    ##pokud to jde, utoc, ale nehraj hned u soupere
    elif("-x--") in pole:
        pozice = (pole.index("x--")) + 2
    elif("--x-") in pole:
        pozice = (pole.index("--x")) + 1

    ## pokud nenajdes peknou volnou sekvenci, hraj takhle:
    elif("x--") in pole:
        pozice = (pole.index("x--")) + 1
    elif("--x") in pole:
        pozice = (pole.index("--x")) + 1

    #nenechej soupere dychat II
    elif("--ox--") in pole:
        pozice = (pole.index("--ox")) + 4
    elif("--xo--") in pole:
        pozice = (pole.index("xo--")) + 1

    # hraj doprostred (pokud nahodou nenastane zadna situace vyse)
    elif("-----") in pole:
        pozice = (pole.index("-----")) + 3
    elif("----") in pole:
        pozice = (pole.index("----")) + 2
    elif("---3") in pole:
        pozice = (pole.index("---")) + 1

    else:
        pozice = randint(0, len(pole) - 1)

    while pole[pozice] != '-':
        pozice = randint(0, len(pole) - 1)
    return tah(pole, pozice, 'x')


def piskvorky1d():
    pole = '-' * 20
    i = 0
    while True:
        if i % 2 == 0:
            pole = tah_hrace(pole)
        else:
            pole = tah_pocitace(pole)
        print(pole)

        if vyhodnot(pole) == 'o':
            print('Vyhral hrac.')
        elif vyhodnot(pole) == 'x':
            print('Vyhral pocitac.')
        elif vyhodnot(pole) == '!':
            print('Remiza!')

        if vyhodnot(pole) != '-':
            break

        i += 1

piskvorky1d()

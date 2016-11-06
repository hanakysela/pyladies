from random import randint, choice


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



def tah_pocitace(pole, symbol):
        """Vrátí herní pole se zaznamenaným tahem počítače."""
        pozice = -1
        cislo=[-1,1]
        if '-' not in pole:
            raise ValueError(print("Pole uz je plne."))
        if symbol=="x":
            opacny_symbol="o"
        elif symbol=="o":
            opacny_symbol="x"
        else:
            raise ValueError(print("Spatny symbol"))

        try:
            o=pole.index(opacny_symbol)
        except:
            while pozice < 0 or pozice >= len(pole) or pole[pozice] != '-':
                pozice = randint(0, len(pole) - 1)
        else:
            indexy = [i for i, x in enumerate(pole) if x == opacny_symbol]
            o=choice(indexy)
            pozice=o+choice(cislo)
            while pozice < 0 or pozice >= len(pole) or pole[pozice] != '-':
                pozice=pozice+choice(cislo)
        return tah(pole, pozice, symbol)


def piskvorky1d():
    pole = '-' * 20
    i = 0
    while True:
        if i % 2 == 0:
            pole = tah_hrace(pole)
        else:
            pole = tah_pocitace(pole, "x")
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

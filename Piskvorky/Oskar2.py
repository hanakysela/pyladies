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
        try:
            pozice = int(input('Kam chces hrat? (0..{})'.format(len(pole) - 1)))
        except ValueError:
            print("To neni cislo")
        else:
            if pozice < 0 or pozice >= len(pole):
                print('Nemuzes hrat venku z pole!')
            elif pole[pozice] != '-':
                print('Tam neni volno!')
            else:
                return tah(pole, pozice, 'o')



def tah_pocitace(pole):
    """Vrati herni pole se zaznamenaným tahem pocitace."""
    pozice = -1
    while pozice < 0 or pozice >= len(pole) or pole[pozice] != '-':
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

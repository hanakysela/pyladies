zvirata = ["pes", "kocka", "andulka", "kralik", "had"]


def rozdvoj(seznam):
    vystupni_seznam = []
    for polozka in seznam:
        dvojice = (polozka[1:], polozka)
        vystupni_seznam.append(dvojice)
    return vystupni_seznam

def sluc(seznam_dvojic):
    vystupni_seznam = []
    for polozka in seznam_dvojic:
        jednice = polozka[1]
        vystupni_seznam.append(jednice)
    return vystupni_seznam

print(zvirata)

dvoj_zvirata = rozdvoj(zvirata)
dvoj_zvirata.sort()
zvirata = sluc(dvoj_zvirata)

print(zvirata)

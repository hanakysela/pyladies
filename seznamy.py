zvirata = ["pes", "kocka", "kralik", "had"]

def vypis5(seznam):
    vystup = []
    for zvire in zvirata:
        if len(zvire) < 5:
            vystup.append(zvire)
    return vystup

nova_zvirata = vypis5(zvirata)

print nova_zvirata

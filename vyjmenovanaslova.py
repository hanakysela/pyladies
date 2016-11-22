a = 'pýcha, pytel, pysk, netopýr, slepýš, pyl, kopyto, klopýtat, třpytit se, zpytovat, pykat, pýr, pýřit se, čepýřit se'
t = 'netopýr nemá kopyto'

a.split(', ')

pocitadlo = 0
for slovo in t.split():
    if slovo in a:
        pocitadlo += 1
    #return pocitadlo
print(pocitadlo)

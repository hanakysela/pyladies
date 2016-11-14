def delitel(od,do):
    seznam = []
    for i in range(od,do):
        if i % 3 == 0:
            seznam.append(i)
    print(len(seznam))
    print(seznam)
    return

delitel(67, 102)

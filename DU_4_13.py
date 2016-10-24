velikost = 5

for i in range (velikost):
    for n in range(velikost):
        if  i == 0 or i == (velikost-1) or n == 0 or n == (velikost-1):
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()

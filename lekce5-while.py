vstup =input("Zadej cislo:")
while not vstup.isdigit():
    print("tohle neni cislo")
    vstup = input("Zadej cislo:")
print("diky, zadal jsi ", vstup, ", diky, cau.")

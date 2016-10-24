tep = int(input("Zadej svuj tep (pocet uderu za minutu)"))

if tep<20:
    print("Procvic si pocitani do stovky a zkontroluj, jestli stopky meri minutu")
elif tep<80:
    print("To je fazona!")
elif tep<120:
    print("Taková nezdravá klasika")
elif tep<180:
    print("to jsou nervy, co?")
else:
    print("Are you sure?")

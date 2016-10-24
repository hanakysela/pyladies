# print("Obvod ctverce se stranou 356 cm je", 356*4, "cm")
# print("Obsah ctverce se stranou 356 cm je", 356**2, "cm2")


# strana = 123 # v centimetrech


strana = int(input("Rekni kolik:")) # int chce integer, kdyby tam to omezeni nebylo,
    # bude to defaulne string, se kterym to pocitat nebude.

cislo_je_OK = strana >= 0

if cislo_je_OK:
    print("Obvod ctverce se stranou", strana, "cm je", strana*4, "cm")
    print("Obsah ctverce se stranou", strana, "cm je", strana**2, "cm2")

else:
    print("Az zadas nezaporne cislo, muzeme se bavit.")

print("Dekujeme, ze nas pouzivate.")

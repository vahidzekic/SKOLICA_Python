#!/usr/bin/env python3
# Grupa7 / 04 / P1 â if/elif/else

print("=== Kategorija putovanja ===")
budzet = int(input("BudÅ¾et (EUR): "))

if budzet >= 2000: kat = "Luksuzno"
elif budzet >= 1000: kat = "Komforno"
elif budzet >= 500: kat = "Standardno"
elif budzet >= 200: kat = "EkonomiÄno"
else: kat = "Backpacking"

print(f"BudÅ¾et: {budzet} EUR -> {kat}")

# LogiÄki
print("\n=== Viza ===")
eje_eu = True
ima_pasos = True
if je_eu or ima_pasos:
    print("Putovanje moguÄe")
else:
    print("Potrebna viza")

print(f"500 EUR je {'dovoljno' if budzet >= 500 else 'nedovoljno'} za Rim")
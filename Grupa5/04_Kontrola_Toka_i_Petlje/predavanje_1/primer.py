#!/usr/bin/env python3
# Grupa5 / 04 / P1 â if/elif/else

print("=== Kategorizacija igraÄa ===")
golovi = int(input("Broj golova: "))

if golovi >= 30: kat = "Zlatna kopaÄka"
elif golovi >= 20: kat = "Zvezdani igraÄ"
elif golovi >= 10: kat = "Solidan strelac"
elif golovi >= 1: kat = "PoÄetnik"
else: kat = "Bez golova"

print(f"Golovi: {golovi} -> {kat}")

# LogiÄki
print("\n=== Pristup ===")
godine = 20
ima_clanarinu = True
if godine >= 18 and ima_clanarinu:
    print("Pristup dozvoljen")
elif godine >= 18:
    print("Platite Älanarinu")
else:
    print("Maloletni")

# Ternary
broj = 15
print(f"{broj} je {'paran' if broj % 2 == 0 else 'neparan'}")
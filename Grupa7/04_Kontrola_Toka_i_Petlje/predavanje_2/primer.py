#!/usr/bin/env python3
# Grupa7 / 04 / P2 â FOR

print("=== Itinerar ===")
dani = ["Istanbul", "Kapadokija", "Pamukkale", "Efes", "Ankara"]
for i, d in enumerate(dani, 1):
    print(f"  Dan {i}: {d}")

print("\n=== range ===")
print(f"Km markeri: {list(range(0, 601, 100))}")
print(f"Odbrojavanje: {list(range(10, 0, -1))}")

print("\n=== zip ===")
gradovi = ["Istanbul", "Dubai", "Rim"]
cene = [200, 450, 180]
for g, c in zip(gradovi, cene):
    zvezdice = '*' * int(c / 100)
    print(f"  {g}: {c}EUR {zvezdice}")

print("\n=== Tabela udaljenosti ===")
gr = ["BEG", "IST", "ROM", "PAR"]
for i in range(len(gr)):
    for j in range(len(gr)):
        print(f"{gr[i]+'-'+gr[j]:>8}", end="")
    print("")
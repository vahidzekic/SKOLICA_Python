#!/usr/bin/env python3
# Grupa5 / 04 / P2 â FOR petlja

planete = ["Merkur","Venera","Zemlja","Mars","Jupiter","Saturn"]
print("=== Planete ===")
for i, p in enumerate(planete, 1):
    print(f"  {i}. {'ð' if p == 'Zemlja' else 'ðª'} {p}")

print("\n=== range ===")
print(f"Parni: {list(range(2, 21, 2))}")
print(f"Obrnuto: {list(range(10, 0, -1))}")

print("\n=== zip ===")
timovi = ["Partizan", "Zvezda", "Vojvodina"]
bodovi = [65, 72, 48]
for tim, bod in zip(timovi, bodovi):
    print(f"  {tim}: {bod} bodova")

print("\n=== Tablica 1-5 ===")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print("")
#!/usr/bin/env python3
# Grupa4 / 04 / P2 â FOR petlja

planete = ["Merkur", "Venera", "Zemlja", "Mars", "Jupiter"]
print("=== Planete ===")
for i, p in enumerate(planete, 1):
    marker = "ð" if p == "Zemlja" else "ðª"
    print(f"  {i}. {marker} {p}")

print("\n=== range() ===")
print("Parni do 20:", [x for x in range(2, 21, 2)])
print("Obrnuto:", list(range(10, 0, -1)))

print("\n=== break ===")
for n in range(1, 100):
    if n % 7 == 0:
        print(f"  Prvi deljiv sa 7: {n}")
        break

print("\n=== Tablica 1-5 ===")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print("")
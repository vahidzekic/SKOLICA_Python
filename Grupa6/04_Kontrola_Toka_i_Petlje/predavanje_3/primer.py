#!/usr/bin/env python3
# Grupa6 / 04 / P3 â WHILE
import random

print("=== Metronom ===")
brojac = 8
while brojac > 0:
    print(f"  Takt {9-brojac}", end=" ")
    brojac -= 1
print("\n")

print("=== while...else ===")
i = 1
while i <= 4:
    print(f"  Strofa {i}")
    i += 1
else:
    print("  Pesma gotova!")

print("\n=== Pogodi pesmu ===")
pesme_igra = ["Imagine", "Yesterday", "Bohemian Rhapsody", "Stairway", "Wonderwall"]
tajna = random.choice(pesme_igra)
for pok in range(1, 4):
    odg = input(f"  PokuÅ¡aj {pok}/3: ")
    if odg.lower() == tajna.lower():
        print(f"  Bravo! '{tajna}'!")
        break
    print(f"  Hint: {tajna[:pok]} ...")
else:
    print(f"  Odgovor: {tajna}")
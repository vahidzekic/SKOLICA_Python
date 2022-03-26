#!/usr/bin/env python3
# Grupa4 / 04 / P3 â WHILE petlja
import random

# Odbrojavanje
print("=== Odbrojavanje ===")
n = 10
while n > 0:
    print(f"  {n}...", end="")
    n -= 1
print(" Lansiranje!")

# while...else
print("\n=== while...else ===")
i = 1
while i <= 5:
    print(f"  Iter {i}")
    i += 1
else:
    print("  Normalan kraj.")

# PogaÄanje broja
print("\n=== Pogodi broj (1-50) ===")
tajna = random.randint(1, 50)
pokusaji = 0
while True:
    odg = int(input("  Tvoj odgovor: "))
    pokusaji += 1
    if odg < tajna: print("  VeÄi!")
    elif odg > tajna: print("  Manji!")
    else:
        print(f"  Bravo! Za {pokusaji} pokuÅ¡aja!")
        break
#!/usr/bin/env python3
# Grupa7 / 04 / P3 â WHILE
import random

print("=== Odbrojavanje do leta ===")
n = 5
while n > 0:
    print(f"  {n}...", end="")
    n -= 1
print(" Poleteli!")

print("\n=== while...else ===")
etapa = 1
while etapa <= 4:
    print(f"  Etapa {etapa} zavrÅ¡ena")
    etapa += 1
else:
    print("  Putovanje zavrÅ¡eno!")

print("\n=== Pogodi grad ===")
gradovi = ["Istanbul", "Rim", "Pariz", "London", "Dubai"]
tajni = random.choice(gradovi)
for pok in range(1, 4):
    odg = input(f"  PokuÅ¡aj {pok}/3: ")
    if odg.lower() == tajni.lower():
        print(f"  Bravo! {tajni}!")
        break
    print(f"  Hint: poÄinje na '{tajni[:pok]}'")
else:
    print(f"  Odgovor: {tajni}")
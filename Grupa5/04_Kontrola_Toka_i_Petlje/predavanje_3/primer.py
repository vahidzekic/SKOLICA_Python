#!/usr/bin/env python3
# Grupa5 / 04 / P3 â WHILE
import random

print("=== Odbrojavanje ===")
n = 5
while n > 0:
    print(f"  {n}...", end="")
    n -= 1
print(" Go!")

print("\n=== while...else ===")
i = 1
while i <= 3:
    print(f"  Krug {i}")
    i += 1
else:
    print("  Trening zavrÅ¡en!")

print("\n=== Pogodi igraÄa (1-30) ===")
tajna = random.randint(1, 30)
for pokusaj in range(1, 6):
    odg = int(input(f"  PokuÅ¡aj {pokusaj}/5: "))
    if odg == tajna:
        print(f"  Bravo! Broj {tajna}!")
        break
    print(f"  {'VeÄi' if odg < tajna else 'Manji'}!")
else:
    print(f"  Game over! Bilo je {tajna}.")
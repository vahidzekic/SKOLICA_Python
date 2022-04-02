#!/usr/bin/env python3
# Grupa4 / 05 / P3 â Moduli
import math, random, datetime, os

print("=== math ===")
print(f"pi={math.pi:.6f}, sqrt(256)={math.sqrt(256)}")

print("\n=== random ===")
print(f"randint(1,6): {random.randint(1,6)}")
boje = ["crvena", "plava", "zelena"]
print(f"choice: {random.choice(boje)}")

print("\n=== datetime ===")
sada = datetime.datetime.now()
print(f"Sada: {sada.strftime('%d.%m.%Y. %H:%M')}")

print(f"\n=== os ===")
print(f"CWD: {os.getcwd()}")

if __name__ == '__main__':
    print("\nDirektno pokretanje.")
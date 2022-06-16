#!/usr/bin/env python3
# Grupa5 / 05 / P3 â Moduli
import math, random, datetime, os

print("=== math ===")
print(f"pi={math.pi:.6f}, e={math.e:.6f}")
print(f"sqrt(625)={math.sqrt(625)}")

print("\n=== random ===")
print(f"randint(1,100): {random.randint(1,100)}")
timovi = ["Partizan", "Zvezda", "Vojvodina", "ÄukariÄki"]
print(f"choice: {random.choice(timovi)}")
random.shuffle(timovi)
print(f"shuffle: {timovi}")

print(f"\n=== datetime ===")
print(f"Sada: {datetime.datetime.now().strftime('%d.%m.%Y. %H:%M')}")

print(f"\n=== os ===")
print(f"CWD: {os.getcwd()}")

if __name__ == '__main__':
    print("\nDirektno pokretanje.")
#!/usr/bin/env python3
# Grupa6 / 05 / P3 â Moduli
import math, random, datetime, os

print("=== math ===")
# Frekvencija note: f = 440 * 2^(n/12)
for n, name in [(-9,"C4"),(0,"A4"),(3,"C5")]:
    print(f"  {name}: {440 * 2**(n/12):.2f} Hz")

print("\n=== random ===")
playlist = ["Imagine", "Yesterday", "Bohemian", "Stairway", "Wonderwall"]
random.shuffle(playlist)
print(f"Shuffle: {playlist}")
print(f"Random: {random.choice(playlist)}")

print(f"\n=== datetime ===")
print(f"Sada: {datetime.datetime.now().strftime('%d.%m.%Y. %H:%M')}")

print(f"\n=== os ===")
print(f"CWD: {os.getcwd()}")

if __name__ == '__main__':
    print("\nDirektno pokretanje.")
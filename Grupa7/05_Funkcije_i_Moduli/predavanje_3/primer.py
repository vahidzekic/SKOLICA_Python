#!/usr/bin/env python3
# Grupa7 / 05 / P3 â Moduli
import math, random, datetime, os

print("=== math ===")
# Haversine approx
print(f"pi={math.pi:.6f}")
print(f"Zemlja R: {6371}km")
print(f"sqrt(40000)={math.sqrt(40000):.1f}")

print("\n=== random ===")
gradovi = ["Istanbul", "Rim", "Pariz", "London"]
print(f"Random: {random.choice(gradovi)}")
random.shuffle(gradovi)
print(f"Shuffle: {gradovi}")

print(f"\n=== datetime ===")
sada = datetime.datetime.now()
print(f"Sada: {sada.strftime('%d.%m.%Y. %H:%M')}")
let = datetime.date(2025, 7, 15)
dana = (let - datetime.date.today()).days
print(f"Do leta: {dana} dana")

print(f"\n=== os ===")
print(f"CWD: {os.getcwd()}")

if __name__ == '__main__':
    print("\nDirektno.")
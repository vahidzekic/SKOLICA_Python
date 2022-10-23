#!/usr/bin/env python3
# Grupa7 / 02 / P3 â Torke
import sys
from collections import namedtuple

print("=== Torke ===")
beograd = (44.7866, 20.4489)
istanbul = (41.0082, 28.9784)
print(f"Beograd: {beograd}")
print(f"Istanbul: {istanbul}")

lat, lon = beograd
print(f"\nLat: {lat}, Lon: {lon}")
prvi, *ostali = (100, 200, 300, 400)
print(f"Prvi: {prvi}, Ostali: {ostali}")

print("\n=== NamedTuple ===")
Grad = namedtuple("Grad", ["ime", "drzava", "populacija"])
gradovi = [
    Grad("Istanbul", "Turska", 16_000_000),
    Grad("London", "UK", 9_000_000),
    Grad("Pariz", "Francuska", 2_200_000),
]
for g in gradovi:
    print(f"  {g.ime} ({g.drzava}): {g.populacija:,}")
najveci = max(gradovi, key=lambda g: g.populacija)
print(f"NajveÄi: {najveci.ime}")

print(f"\nMemorija: Lista={sys.getsizeof([1,2,3])}B, Torka={sys.getsizeof((1,2,3))}B")

# Torka kao kljuÄ
dist = {("Beograd","Istanbul"): 594, ("Beograd","Rim"): 1060}
for (a,b), km in dist.items():
    print(f"  {a} -> {b}: {km}km")
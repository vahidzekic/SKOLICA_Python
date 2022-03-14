#!/usr/bin/env python3
# Grupa4 / 02 / Predavanje 3 — Torke
import sys
from collections import namedtuple

# Kreiranje
print("=== Torke ===")
koord = (44.01, 20.92)
rgb = (255, 128, 0)
print(f"Koordinate: {koord}")
print(f"RGB: {rgb}")
print("")

# Unpacking
print("=== Unpacking ===")
lat, lon = koord
print(f"Lat: {lat}, Lon: {lon}")
prva, *ostale, poslednja = (10, 20, 30, 40, 50)
print(f"Prva: {prva}, Ostale: {ostale}, Poslednja: {poslednja}")
x, y = 100, 200
x, y = y, x
print(f"Swap: x={x}, y={y}")
print("")

# Named tuple
print("=== NamedTuple ===")
Student = namedtuple("Student", ["ime", "prezime", "prosek"])
studenti = [Student("Vahid","Zekic",9.2), Student("Enes","Daca",8.5), Student("Kemo","P",9.7)]
for s in studenti:
    print(f"  {s.ime} {s.prezime}: {s.prosek}")
print(f"Najbolji: {max(studenti, key=lambda s: s.prosek).ime}")
print("")

# Memorija
print("=== Memorija ===")
l = [1,2,3,4,5]
t = (1,2,3,4,5)
print(f"Lista: {sys.getsizeof(l)}B, Torka: {sys.getsizeof(t)}B")

# Dict ključ
print("\n=== Torka kao dict ključ ===")
dist = {("Beograd","Novi Pazar"): 290, ("Beograd","Niš"): 240}
for (g1,g2), km in dist.items():
    print(f"  {g1} <-> {g2}: {km}km")

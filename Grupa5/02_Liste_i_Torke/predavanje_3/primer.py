#!/usr/bin/env python3
# Grupa5 / 02 / P3 â Torke
import sys
from collections import namedtuple

print("=== Torke ===")
resultat = (3, 1)  # rezultat utakmice
rgb = (0, 128, 255)
print(f"Rezultat: {rezultat}")
print(f"RGB: {rgb}")

# Unpacking
domacin, gost = rezultat
print(f"\nDomaÄin: {domacin}, Gost: {gost}")
prva, *ostale = (10, 20, 30, 40, 50)
print(f"Prva: {prva}, Ostale: {ostale}")

# Named tuple
print("\n=== NamedTuple ===")
Igrac = namedtuple("Igrac", ["ime", "tim", "golovi"])
igraci = [Igrac("JoviÄ","Real",12), Igrac("VlahoviÄ","Juve",24), Igrac("MitroviÄ","Al Hilal",18)]
for ig in igraci:
    print(f"  {ig.ime} ({ig.tim}): {ig.golovi} golova")
najbolji = max(igraci, key=lambda i: i.golovi)
print(f"Najbolji: {najbolji.ime}")

print(f"\nMemorija: Lista={sys.getsizeof([1,2,3])}B, Torka={sys.getsizeof((1,2,3))}B")
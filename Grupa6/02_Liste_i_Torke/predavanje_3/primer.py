#!/usr/bin/env python3
# Grupa6 / 02 / P3 â Torke
import sys
from collections import namedtuple

print("=== Torke ===")
nota = ("Do", 261.63)  # nota i frekvencija
rgb_crvena = (255, 0, 0)
print(f"Nota: {nota}")
print(f"RGB: {rgb_crvena}")

# Unpacking
ime_note, frekvencija = nota
print(f"\nNota: {ime_note}, Hz: {frekvencija}")
prva, *ostale = (1, 2, 3, 4, 5)
print(f"Prva: {prva}, Ostale: {ostale}")

# NamedTuple
print("\n=== NamedTuple ===")
Pesma = namedtuple("Pesma", ["naziv", "autor", "trajanje"])
playlist = [
    Pesma("Imagine", "Lennon", 3.03),
    Pesma("Yesterday", "Beatles", 2.05),
    Pesma("Bohemian", "Queen", 5.55),
]
for p in playlist:
    print(f"  {p.naziv} â {p.autor} ({p.trajanje}min)")
najduza = max(playlist, key=lambda p: p.trajanje)
print(f"NajduÅ¾a: {najduza.naziv}")

print(f"\nMemorija: Lista={sys.getsizeof([1,2,3])}B, Torka={sys.getsizeof((1,2,3))}B")
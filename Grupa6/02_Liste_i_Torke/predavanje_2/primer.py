#!/usr/bin/env python3
# Grupa6 / 02 / P2 â Comprehension

print("=== Comprehension ===")
kvadr = [x**2 for x in range(1, 11)]
print(f"Kvadrati: {kvadr}")
parni = [x for x in range(2, 21, 2)]
print(f"Parni: {parni}")
pesme = ["yesterday", "imagine", "bohemian rhapsody"]
print(f"Title: {[p.title() for p in pesme]}")

print("\n=== enumerate ===")
for i, p in enumerate(pesme, 1):
    print(f"  {i}. {p.title()}")

print("\n=== zip ===")
albumi = ["Dark Side", "The Wall", "Wish You Were Here"]
godine = [1973, 1979, 1975]
for a, g in zip(albumi, godine):
    print(f"  {a} ({g})")

print("\n=== Matrica ===")
m = [[1,2,3],[4,5,6],[7,8,9]]
for r in m: print(f"  {r}")
print(f"Flat: {[e for r in m for e in r]}")
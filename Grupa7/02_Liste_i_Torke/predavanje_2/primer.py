#!/usr/bin/env python3
# Grupa7 / 02 / P2 â Comprehension

print("=== Comprehension ===")
km = [594, 4200, 1060, 1700, 1900]
milje = [round(k * 0.621, 1) for k in km]
print(f"KM: {km}")
print(f"Milje: {milje}")

blizu = [k for k in km if k < 1500]
print(f"Blizu (<1500): {blizu}")

print("\n=== enumerate ===")
grad = ["Istanbul", "Dubai", "Rim", "Pariz"]
for i, g in enumerate(grad, 1):
    print(f"  {i}. {g}")

print("\n=== zip ===")
for g, k in zip(grad, km[:4]):
    cena = round(k * 0.12)
    print(f"  {g}: {k}km, ~{cena} EUR")

print("\n=== Matrica ===")
m = [[1,0,1],[0,1,0],[1,1,1]]
for r in m: print(f"  {r}")
print(f"Flat: {[e for r in m for e in r]}")
#!/usr/bin/env python3
# Grupa5 / 02 / P2 â Comprehension

print("=== Comprehension ===")
stepeni = [x**2 for x in range(1, 11)]
print(f"Kvadrati: {stepeni}")
neparni = [x for x in range(1, 21) if x % 2 != 0]
print(f"Neparni: {neparni}")
reci = ["python", "java", "go", "rust"]
print(f"Cap: {[r.capitalize() for r in reci]}")

print("\n=== enumerate ===")
for i, r in enumerate(reci, 1):
    print(f"  {i}. {r}")

print("\n=== zip ===")
igraci = ["JoviÄ", "MitroviÄ", "VlahoviÄ"]
golovi = [12, 18, 24]
for igrac, gol in zip(igraci, golovi):
    print(f"  {igrac}: {gol} golova")

print("\n=== Matrica ===")
m = [[1,2,3],[4,5,6],[7,8,9]]
for r in m: print(f"  {r}")
flat = [e for r in m for e in r]
print(f"Flat: {flat}")
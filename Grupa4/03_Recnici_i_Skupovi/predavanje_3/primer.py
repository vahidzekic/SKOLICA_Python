#!/usr/bin/env python3
# Grupa4 / 03 / P3 â Comprehension, Counter
from collections import Counter, defaultdict

# Dict comprehension
fahrenheit = {c: round(c*9/5+32, 1) for c in range(0, 101, 10)}
print("=== C -> F ===")
for c, f in fahrenheit.items():
    print(f"  {c}C = {f}F")

# Counter
print("\n=== Counter ===")
slova = Counter("abracadabra")
print(f"Slova: {dict(slova)}")
print(f"Top 3: {slova.most_common(3)}")

# defaultdict
print("\n=== defaultdict ===")
po_oceni = defaultdict(list)
for ime, oc in [("Enes",9),("Kemo",10),("Ahmed",8),("Vahid",9)]:
    po_oceni[oc].append(ime)
for oc in sorted(po_oceni, reverse=True):
    print(f"  Ocena {oc}: {po_oceni[oc]}")
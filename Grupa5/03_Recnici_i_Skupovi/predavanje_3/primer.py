#!/usr/bin/env python3
# Grupa5 / 03 / P3 â Comprehension, Counter
from collections import Counter, defaultdict

print("=== Dict Comprehension ===")
km_milje = {km: round(km * 0.621, 1) for km in range(10, 101, 10)}
for km, mi in km_milje.items():
    print(f"  {km}km = {mi}mi")

print("\n=== Counter ===")
golovi = ["MitroviÄ", "JoviÄ", "MitroviÄ", "VlahoviÄ", "JoviÄ", "MitroviÄ"]
brojac = Counter(golovi)
print(f"Golovi: {dict(brojac)}")
print(f"Top 2: {brojac.most_common(2)}")

print("\n=== defaultdict ===")
po_poziciji = defaultdict(list)
igraci = [("GK","RajkoviÄ"),("DEF","PavloviÄ"),("MID","MilinkoviÄ"),("FW","MitroviÄ"),("FW","JoviÄ")]
for poz, ime in igraci:
    po_poziciji[poz].append(ime)
for poz, imena in po_poziciji.items():
    print(f"  {poz}: {imena}")
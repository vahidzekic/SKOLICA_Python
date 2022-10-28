#!/usr/bin/env python3
# Grupa7 / 03 / P3 â Comprehension, Counter
from collections import Counter, defaultdict

print("=== Dict Comprehension ===")
km_to_mi = {km: round(km * 0.621, 1) for km in range(100, 1001, 100)}
for km, mi in km_to_mi.items():
    print(f"  {km}km = {mi}mi")

print("\n=== Counter ===")
kontinenti = ["Evropa","Azija","Evropa","Afrika","Evropa","Azija","Evropa","Azija"]
br = Counter(kontinenti)
print(f"Posete: {dict(br)}")
print(f"Top 2: {br.most_common(2)}")

print("\n=== defaultdict ===")
po_kontinentu = defaultdict(list)
gradovi = [("Evropa","Rim"),("Azija","Istanbul"),("Evropa","Pariz"),("Afrika","Kairo"),("Azija","Dubai")]
for kont, grad in gradovi:
    po_kontinentu[kont].append(grad)
for k, gs in po_kontinentu.items():
    print(f"  {k}: {gs}")
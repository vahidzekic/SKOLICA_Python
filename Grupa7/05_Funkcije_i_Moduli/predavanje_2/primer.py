#!/usr/bin/env python3
# Grupa7 / 05 / P2 â Lambda, map, filter

print("=== Lambda ===")
km2mi = lambda km: round(km * 0.621, 1)
print(f"1000km = {km2mi(1000)}mi")

print("\n=== map ===")
udaljenosti = [594, 1060, 1700, 4200]
milje = list(map(lambda k: round(k * 0.621), udaljenosti))
print(f"KM: {udaljenosti}")
print(f"Mi: {milje}")

print("\n=== filter ===")
cene = [99, 350, 180, 500, 75, 420]
jeftini = list(filter(lambda c: c <= 200, cene))
skupi = list(filter(lambda c: c > 200, cene))
print(f"Sve: {cene}")
print(f"Jeftini (<=200): {jeftini}")
print(f"Skupi (>200): {skupi}")

print("\n=== sorted ===")
dest = [("Istanbul",594),("Dubai",4200),("Rim",1060),("Pariz",1700)]
print(f"Po km: {sorted(dest, key=lambda d: d[1])}")
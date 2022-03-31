#!/usr/bin/env python3
# Grupa4 / 05 / P2 â Lambda, map, filter

print("=== Lambda ===")
kv = lambda x: x**2
print(f"kv(9) = {kv(9)}")

print("\n=== map ===")
cene = [10, 25, 50, 100]
rsd = list(map(lambda c: round(c*117.5), cene))
print(f"EUR: {cene}")
print(f"RSD: {rsd}")

print("\n=== filter ===")
ocene = [5, 7, 4, 9, 6, 3, 8, 10]
polozili = list(filter(lambda o: o >= 6, ocene))
print(f"Ocene: {ocene}")
print(f"PoloÅ¾ili: {polozili}")

print("\n=== sorted ===")
timovi = [("A",25),("B",30),("C",18),("D",28)]
print(f"Po poenima: {sorted(timovi, key=lambda t: t[1], reverse=True)}")
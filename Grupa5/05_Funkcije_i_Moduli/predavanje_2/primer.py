#!/usr/bin/env python3
# Grupa5 / 05 / P2 â Lambda, map, filter

print("=== Lambda ===")
kvadrat = lambda x: x**2
print(f"kvadrat(8) = {kvadrat(8)}")

print("\n=== map ===")
temperature_c = [0, 10, 20, 30, 40]
temperature_f = list(map(lambda c: round(c * 9/5 + 32, 1), temperature_c))
print(f"C: {temperature_c}")
print(f"F: {temperature_f}")

print("\n=== filter ===")
broj_golova = [2, 0, 5, 1, 0, 3, 0, 7]
strelci = list(filter(lambda g: g > 0, broj_golova))
print(f"Svi: {broj_golova}")
print(f"Strelci: {strelci}")

print("\n=== sorted ===")
igraci = [("JoviÄ", 12), ("MitroviÄ", 18), ("VlahoviÄ", 24)]
po_golova = sorted(igraci, key=lambda x: x[1], reverse=True)
print(f"Po golovima: {po_golova}")
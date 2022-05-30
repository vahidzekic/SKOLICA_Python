#!/usr/bin/env python3
# Grupa5 / 03 / P1 â ReÄnici

recept = {
    "naziv": "Äevapi",
    "poreklo": "Balkan",
    "vreme_min": 30,
    "porcija": 4,
    "sastojci": ["meso", "luk", "so", "biber"]
}

print("=== Recept ===")
for k, v in recept.items():
    print(f"  {k}: {v}")

# CRUD
recept["kalorije"] = 450
recept["vreme_min"] = 25
del recept["porcija"]
print(f"\nAÅ¾uriran: {recept}")
print(f"Poreklo: {recept.get('poreklo', 'N/A')}")
print(f"Cena: {recept.get('cena', 'Nepoznata')}")

# Lista reÄnika
recepti = [
    {"naziv": "Äevapi", "vreme": 30, "ocena": 4.8},
    {"naziv": "Burek", "vreme": 60, "ocena": 4.9},
    {"naziv": "Sarma", "vreme": 120, "ocena": 4.7},
]
print("\n=== Recepti po oceni ===")
for r in sorted(recepti, key=lambda x: x["ocena"], reverse=True):
    print(f"  {r['ocena']} - {r['naziv']} ({r['vreme']}min)")
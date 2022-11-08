#!/usr/bin/env python3
# Grupa7 / 06 / P2 â JSON
import json, os
os.makedirs('data', exist_ok=True)

destinacije = [
    {"grad": "Istanbul", "drzava": "Turska", "km": 594, "cena": 200},
    {"grad": "Rim", "drzava": "Italija", "km": 1060, "cena": 180},
    {"grad": "Pariz", "drzava": "Francuska", "km": 1700, "cena": 250},
]

with open('data/destinacije.json', 'w', encoding='utf-8') as f:
    json.dump(destinacije, f, indent=4, ensure_ascii=False)
print(f'Zapisano {len(destinacije)}')

with open('data/destinacije.json', 'r', encoding='utf-8') as f:
    ucitane = json.load(f)
for d in ucitane:
    print(f"  {d['grad']} ({d['drzava']}): {d['km']}km, {d['cena']}EUR")

ucitane.append({"grad": "London", "drzava": "UK", "km": 1900, "cena": 280})
with open('data/destinacije.json', 'w', encoding='utf-8') as f:
    json.dump(ucitane, f, indent=4, ensure_ascii=False)
print(f'AÅ¾urirano: {len(ucitane)}')
#!/usr/bin/env python3
# Grupa6 / 06 / P2 â JSON
import json, os
os.makedirs('data', exist_ok=True)

albumi = [
    {"naziv": "Abbey Road", "bend": "Beatles", "god": 1969, "ocena": 9.8},
    {"naziv": "Dark Side", "bend": "Pink Floyd", "god": 1973, "ocena": 9.9},
    {"naziv": "Thriller", "bend": "M. Jackson", "god": 1982, "ocena": 9.5},
]

with open('data/albumi.json', 'w', encoding='utf-8') as f:
    json.dump(albumi, f, indent=4, ensure_ascii=False)
print(f'Zapisano {len(albumi)} albuma')

with open('data/albumi.json', 'r', encoding='utf-8') as f:
    ucitani = json.load(f)
for a in ucitani:
    print(f"  {a['ocena']} â {a['naziv']} ({a['bend']}, {a['god']})")

ucitani.append({"naziv": "OK Computer", "bend": "Radiohead", "god": 1997, "ocena": 9.6})
with open('data/albumi.json', 'w', encoding='utf-8') as f:
    json.dump(ucitani, f, indent=4, ensure_ascii=False)
print(f'AÅ¾urirano: {len(ucitani)}')
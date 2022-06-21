#!/usr/bin/env python3
# Grupa5 / 06 / P2 â JSON
import json, os
os.makedirs('data', exist_ok=True)

igraci = [
    {"ime": "JoviÄ", "tim": "Milan", "golovi": 12},
    {"ime": "MitroviÄ", "tim": "Al Hilal", "golovi": 18},
    {"ime": "VlahoviÄ", "tim": "Juve", "golovi": 24},
]

with open('data/igraci.json', 'w', encoding='utf-8') as f:
    json.dump(igraci, f, indent=4, ensure_ascii=False)
print(f'Zapisano {len(igraci)} igraÄa')

with open('data/igraci.json', 'r', encoding='utf-8') as f:
    ucitani = json.load(f)
for ig in ucitani:
    print(f"  {ig['ime']} ({ig['tim']}): {ig['golovi']} golova")

ucitani.append({"ime": "TadiÄ", "tim": "FenerbahÄe", "golovi": 15})
with open('data/igraci.json', 'w', encoding='utf-8') as f:
    json.dump(ucitani, f, indent=4, ensure_ascii=False)
print(f'AÅ¾urirano: {len(ucitani)}')
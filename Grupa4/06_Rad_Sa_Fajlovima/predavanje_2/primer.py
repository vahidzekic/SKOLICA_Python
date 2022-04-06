#!/usr/bin/env python3
# Grupa4 / 06 / P2 â JSON
import json, os
os.makedirs('data', exist_ok=True)

biblioteka = [
    {"naslov": "Python Crash Course", "autor": "Matthes", "str": 544},
    {"naslov": "Fluent Python", "autor": "Ramalho", "str": 792},
    {"naslov": "Clean Code", "autor": "Martin", "str": 464},
]

with open('data/knjige.json', 'w', encoding='utf-8') as f:
    json.dump(biblioteka, f, indent=4, ensure_ascii=False)
print(f'Zapisano {len(biblioteka)} knjiga')

with open('data/knjige.json', 'r', encoding='utf-8') as f:
    knjige = json.load(f)
for k in knjige:
    print(f"  {k['naslov']} â {k['autor']}")

knjige.append({"naslov": "Automate", "autor": "Sweigart", "str": 592})
with open('data/knjige.json', 'w', encoding='utf-8') as f:
    json.dump(knjige, f, indent=4, ensure_ascii=False)
print(f'AÅ¾urirano: {len(knjige)}')
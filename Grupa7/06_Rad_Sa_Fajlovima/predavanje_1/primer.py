#!/usr/bin/env python3
# Grupa7 / 06 / P1 â Tekst
import os
os.makedirs('data', exist_ok=True)

with open('data/itinerar.txt', 'w', encoding='utf-8') as f:
    f.write('Itinerar â Turska 2025\n')
    f.write('=' * 25 + '\n')
    dani = ["Istanbul", "Kapadokija", "Pamukkale", "Efes", "Ankara"]
    for i, d in enumerate(dani, 1):
        f.write(f'Dan {i}: {d}\n')
print('Kreiran')

with open('data/itinerar.txt', 'r', encoding='utf-8') as f:
    for br, lin in enumerate(f, 1):
        print(f'  [{br}] {lin.rstrip()}')

with open('data/itinerar.txt', 'a', encoding='utf-8') as f:
    f.write('Dan 6: Povratak\n')
print('Dodata linija')
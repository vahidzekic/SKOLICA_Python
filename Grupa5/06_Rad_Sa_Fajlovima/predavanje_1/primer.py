#!/usr/bin/env python3
# Grupa5 / 06 / P1 â Tekst fajlovi
import os
os.makedirs('data', exist_ok=True)

with open('data/trening.txt', 'w', encoding='utf-8') as f:
    f.write('Trening dnevnik\n')
    f.write('=' * 25 + '\n')
    for d in range(1, 8):
        f.write(f'Dan {d}: Trening zavrÅ¡en\n')
print('Kreiran')

with open('data/trening.txt', 'r', encoding='utf-8') as f:
    for br, lin in enumerate(f, 1):
        print(f'  [{br}] {lin.rstrip()}')

with open('data/trening.txt', 'a', encoding='utf-8') as f:
    f.write('Dan 8: Odmor\n')
print('Dodata linija')
#!/usr/bin/env python3
# Grupa4 / 06 / P1 â Tekst fajlovi
import os
os.makedirs('data', exist_ok=True)

with open('data/dnevnik.txt', 'w', encoding='utf-8') as f:
    f.write('Å KOLICA Dnevnik\n')
    for d in range(1, 8):
        f.write(f'Dan {d}: Lekcija OK\n')
print('Kreiran')

with open('data/dnevnik.txt', 'r', encoding='utf-8') as f:
    for br, lin in enumerate(f, 1):
        print(f'  [{br}] {lin.rstrip()}')

with open('data/dnevnik.txt', 'a', encoding='utf-8') as f:
    f.write('Dan 8: Ponavljanje\n')
print('Dodata linija')
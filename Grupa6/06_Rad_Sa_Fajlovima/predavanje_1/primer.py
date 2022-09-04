#!/usr/bin/env python3
# Grupa6 / 06 / P1 â Tekst
import os
os.makedirs('data', exist_ok=True)

with open('data/playlist.txt', 'w', encoding='utf-8') as f:
    f.write('Moja Playlist\n')
    f.write('=' * 20 + '\n')
    pesme = ["Imagine", "Yesterday", "Bohemian Rhapsody", "Stairway to Heaven"]
    for i, p in enumerate(pesme, 1):
        f.write(f'{i}. {p}\n')
print('Kreiran')

with open('data/playlist.txt', 'r', encoding='utf-8') as f:
    for br, lin in enumerate(f, 1):
        print(f'  [{br}] {lin.rstrip()}')

with open('data/playlist.txt', 'a', encoding='utf-8') as f:
    f.write('5. Hotel California\n')
print('Dodata pesma')
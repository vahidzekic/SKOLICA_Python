#!/usr/bin/env python3
# Grupa5 / 06 / P3 â CSV, os
import csv, os
os.makedirs('data', exist_ok=True)

redovi = [["Tim","Bodovi","Golovi"],["Partizan",65,48],["Zvezda",72,55],["Vojvodina",48,32]]
with open('data/liga.csv', 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(redovi)
print('CSV kreiran')

with open('data/liga.csv', 'r', encoding='utf-8') as f:
    for red in csv.DictReader(f):
        print(f"  {red['Tim']}: {red['Bodovi']}b, {red['Golovi']}g")

print(f"\nFajlovi u data/:")
for fn in os.listdir('data'):
    print(f"  {fn} ({os.path.getsize(os.path.join('data',fn))}B)")
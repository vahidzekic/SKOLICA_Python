#!/usr/bin/env python3
# Grupa6 / 06 / P3 â CSV, os
import csv, os
os.makedirs('data', exist_ok=True)

redovi = [["Pesma","Bend","Godina"],["Imagine","Lennon",1971],["Yesterday","Beatles",1965],["Bohemian","Queen",1975]]
with open('data/pesme.csv', 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(redovi)
print('CSV kreiran')

with open('data/pesme.csv', 'r', encoding='utf-8') as f:
    for red in csv.DictReader(f):
        print(f"  {red['Pesma']} â {red['Bend']} ({red['Godina']})")

print(f"\nFajlovi u data/:")
for fn in os.listdir('data'):
    print(f"  {fn} ({os.path.getsize(os.path.join('data',fn))}B)")
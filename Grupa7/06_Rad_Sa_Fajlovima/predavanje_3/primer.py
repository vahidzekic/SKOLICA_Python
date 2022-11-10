#!/usr/bin/env python3
# Grupa7 / 06 / P3 â CSV, os
import csv, os
os.makedirs('data', exist_ok=True)

redovi = [["Grad","Km","Cena"],["Istanbul",594,200],["Rim",1060,180],["Pariz",1700,250]]
with open('data/rute.csv', 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(redovi)
print('CSV kreiran')

with open('data/rute.csv', 'r', encoding='utf-8') as f:
    for red in csv.DictReader(f):
        print(f"  {red['Grad']}: {red['Km']}km, {red['Cena']}EUR")

print(f"\nFajlovi u data/:")
for fn in os.listdir('data'):
    print(f"  {fn} ({os.path.getsize(os.path.join('data',fn))}B)")
#!/usr/bin/env python3
# Grupa4 / 06 / P3 â CSV i os
import csv, os
os.makedirs('data', exist_ok=True)

redovi = [["Ime","Jezik","God"],["Vahid","Python",5],["Enes","JS",3],["Kemo","Go",2]]
with open('data/programeri.csv', 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(redovi)
print('CSV kreiran')

with open('data/programeri.csv', 'r', encoding='utf-8') as f:
    for red in csv.DictReader(f):
        print(f"  {red['Ime']} -> {red['Jezik']}")

print(f"\nFajlovi u data/:")
for fn in os.listdir('data'):
    print(f"  {fn} ({os.path.getsize(os.path.join('data',fn))}B)")
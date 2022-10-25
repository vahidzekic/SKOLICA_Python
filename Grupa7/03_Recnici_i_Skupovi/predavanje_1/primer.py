#!/usr/bin/env python3
# Grupa7 / 03 / P1 â ReÄnici

destinacija = {
    "grad": "Istanbul",
    "drzava": "Turska",
    "kontinent": "Evropa/Azija",
    "populacija": 16_000_000,
    "znamenitosti": ["Aja Sofija", "Plava DÅ¾amija", "Topkapi"]
}

print("=== Destinacija ===")
for k, v in destinacija.items():
    print(f"  {k}: {v}")

destinacija["valuta"] = "TRY"
destinacija["populacija"] = 16_500_000
del destinacija["kontinent"]
print(f"\nAÅ¾urirano: {destinacija}")
print(f"Klima: {destinacija.get('klima', 'Nepoznata')}")

dest_list = [
    {"grad": "Istanbul", "cena": 200, "ocena": 4.8},
    {"grad": "Dubai", "cena": 450, "ocena": 4.6},
    {"grad": "Rim", "cena": 180, "ocena": 4.9},
]
print("\n=== Po oceni ===")
for d in sorted(dest_list, key=lambda x: x["ocena"], reverse=True):
    print(f"  {d['ocena']} â {d['grad']} ({d['cena']} EUR)")
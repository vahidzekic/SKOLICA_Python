#!/usr/bin/env python3
# Grupa6 / 03 / P1 â ReÄnici

knjiga = {
    "naslov": "1984",
    "autor": "George Orwell",
    "godina": 1949,
    "strana": 328,
    "zanr": "Distopija"
}

print("=== Knjiga ===")
for k, v in knjiga.items():
    print(f"  {k}: {v}")

knjiga["isbn"] = "978-0451524935"
knjiga["strana"] = 336
del knjiga["zanr"]
print(f"\nAÅ¾urirano: {knjiga}")
print(f"IzdavaÄ: {knjiga.get('izdavac', 'Nepoznat')}")

knjige = [
    {"naslov": "1984", "god": 1949, "ocena": 4.7},
    {"naslov": "Brave New World", "god": 1932, "ocena": 4.3},
    {"naslov": "Fahrenheit 451", "god": 1953, "ocena": 4.5},
]
print("\n=== Po oceni ===")
for k in sorted(knjige, key=lambda x: x["ocena"], reverse=True):
    print(f"  {k['ocena']} â {k['naslov']} ({k['god']})")
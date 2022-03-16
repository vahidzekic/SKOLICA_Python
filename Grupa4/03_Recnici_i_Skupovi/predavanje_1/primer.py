#!/usr/bin/env python3
# Grupa4 / 03 / P1 â ReÄnici

film = {
    "naslov": "Inception",
    "reziser": "Christopher Nolan",
    "godina": 2010,
    "ocena": 8.8,
    "zanrovi": ["Sci-Fi", "Triler"]
}

print("=== Film ===")
for k, v in film.items():
    print(f"  {k}: {v}")

# CRUD
film["trajanje"] = 148
film["ocena"] = 9.0
del film["zanrovi"]
print(f"\nAÅ¾uriran: {film}")
print(f"BudÅ¾et: {film.get('budzet', 'Nepoznat')}")

# Lista reÄnika
filmovi = [
    {"naslov": "Inception", "god": 2010, "ocena": 8.8},
    {"naslov": "Interstellar", "god": 2014, "ocena": 8.7},
    {"naslov": "The Dark Knight", "god": 2008, "ocena": 9.0},
]
print("\n=== Filmoteka ===")
for f in sorted(filmovi, key=lambda x: x["ocena"], reverse=True):
    print(f"  {f['ocena']} - {f['naslov']} ({f['god']})")
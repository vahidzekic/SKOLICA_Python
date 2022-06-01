#!/usr/bin/env python3
# Grupa5 / 03 / P2 â Skupovi

python_ucenici = {"Ana", "Marko", "Jovan", "Milica"}
js_ucenici = {"Marko", "Petar", "Ana", "Nikola"}

print("=== Set operacije ===")
print(f"Python: {python_ucenici}")
print(f"JS: {js_ucenici}")
print(f"Oba: {python_ucenici & js_ucenici}")
print(f"Svi: {python_ucenici | js_ucenici}")
print(f"Samo Py: {python_ucenici - js_ucenici}")
print(f"Samo JS: {js_ucenici - python_ucenici}")

# Duplikati
narudzbine = ["kafa", "Äaj", "kafa", "sok", "Äaj", "voda"]
print(f"\nBez duplikata: {list(set(narudzbine))}")

# Provera
dozvoljeni = {".py", ".js", ".html", ".css"}
fajl = "app.py"
ext = "." + fajl.split(".")[-1]
print(f"'{fajl}' dozvoljen: {ext in dozvoljeni}")
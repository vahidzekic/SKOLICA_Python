#!/usr/bin/env python3
# Grupa4 / 02 / Predavanje 1 — Liste osnove

gradovi = ["Beograd", "Novi Sad", "Niš", "Kragujevac", "Novi Pazar"]
ocene = [8, 9, 7, 10, 6, 9, 8]

print("=== Liste ===")
print(f"Gradovi: {gradovi}")
print(f"Dužina: {len(gradovi)}")
print(f"Prvi: {gradovi[0]}, Poslednji: {gradovi[-1]}")
print(f"Slice [1:3]: {gradovi[1:3]}")
print(f"Obrnuto: {gradovi[::-1]}")
print("")

# CRUD
jezici = ["Python", "C", "Java"]
print("=== CRUD ===")
print(f"Start: {jezici}")
jezici.append("JavaScript")
print(f"append: {jezici}")
jezici.insert(2, "Go")
print(f"insert: {jezici}")
jezici.remove("Java")
print(f"remove: {jezici}")
izbacen = jezici.pop(1)
print(f"pop(1)->'{izbacen}': {jezici}")
print("")

# Sortiranje
print("=== Sort ===")
ocene.sort()
print(f"Sortirane: {ocene}")
print(f"min={min(ocene)}, max={max(ocene)}, avg={sum(ocene)/len(ocene):.1f}")

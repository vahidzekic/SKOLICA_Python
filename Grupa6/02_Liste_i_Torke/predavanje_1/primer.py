#!/usr/bin/env python3
# Grupa6 / 02 / P1 â Liste

bendovi = ["Queen", "Pink Floyd", "Led Zeppelin", "Nirvana", "Radiohead"]
ocene = [9, 10, 9, 8, 10]

print("=== Liste ===")
print(f"Bendovi: {bendovi}")
print(f"DuÅ¾ina: {len(bendovi)}")
print(f"Prvi: {bendovi[0]}, Poslednji: {bendovi[-1]}")
print(f"Slice [1:3]: {bendovi[1:3]}")
print(f"Obrnuto: {bendovi[::-1]}")

# CRUD
bendovi.append("Metallica")
print(f"\nappend: {bendovi}")
bendovi.insert(2, "AC/DC")
print(f"insert: {bendovi}")
bendovi.remove("Nirvana")
print(f"remove: {bendovi}")

ocene.sort(reverse=True)
print(f"\nOcene sort: {ocene}")
print(f"Avg: {sum(ocene)/len(ocene):.1f}")
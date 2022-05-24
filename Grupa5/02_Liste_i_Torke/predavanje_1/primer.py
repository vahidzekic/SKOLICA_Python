#!/usr/bin/env python3
# Grupa5 / 02 / P1 â Liste

timovi = ["Partizan", "Zvezda", "Vojvodina", "ÄukariÄki", "Novi Pazar"]
poeni = [45, 52, 38, 41, 29]

print("=== Liste ===")
print(f"Timovi: {timovi}")
print(f"DuÅ¾ina: {len(timovi)}")
print(f"Prvi: {timovi[0]}, Poslednji: {timovi[-1]}")
print(f"Slice [1:3]: {timovi[1:3]}")
print(f"Obrnuto: {timovi[::-1]}")

# CRUD
timovi.append("OFK")
print(f"\nappend: {timovi}")
timovi.insert(2, "RadniÄki")
print(f"insert: {timovi}")
timovi.remove("OFK")
print(f"remove: {timovi}")

# Sort
poeni.sort(reverse=True)
print(f"\nSortirano: {poeni}")
print(f"Max={max(poeni)}, Min={min(poeni)}, Avg={sum(poeni)/len(poeni):.1f}")
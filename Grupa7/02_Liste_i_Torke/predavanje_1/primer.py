#!/usr/bin/env python3
# Grupa7 / 02 / P1 â Liste

destinacije = ["Istanbul", "Dubai", "Rim", "Pariz", "London"]
udaljenosti = [594, 4200, 1060, 1700, 1900]

print("=== Liste ===")
print(f"Destinacije: {destinacije}")
print(f"DuÅ¾ina: {len(destinacije)}")
print(f"Prvi: {destinacije[0]}, Poslednji: {destinacije[-1]}")
print(f"Slice [1:3]: {destinacije[1:3]}")
print(f"Obrnuto: {destinacije[::-1]}")

# CRUD
destinacije.append("Barselona")
print(f"\nappend: {destinacije}")
destinacije.insert(2, "Atina")
print(f"insert: {destinacije}")
destinacije.remove("Dubai")
print(f"remove: {destinacije}")

udaljenosti.sort()
print(f"\nSortirane: {udaljenosti}")
print(f"Min={min(udaljenosti)}, Max={max(udaljenosti)}, Avg={sum(udaljenosti)/len(udaljenosti):.0f}")
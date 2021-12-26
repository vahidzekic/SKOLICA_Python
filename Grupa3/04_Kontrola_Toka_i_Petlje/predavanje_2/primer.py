#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 04_Kontrola_Toka_i_Petlje / Predavanje 2
# Tema: FOR petlja, range(), enumerate(), zip(), break/continue
# =============================================================================

# --- 1. OSNOVNA FOR PETLJA ---
print("=== Iteracija kroz listu ===")
voce = ["jabuka", "banana", "višnja", "narandža"]
for v in voce:
    print(f"  🍎 {v}")
print("")

# --- 2. range() ---
print("=== range() primeri ===")
print("range(5):", list(range(5)))
print("range(3,8):", list(range(3, 8)))
print("range(0,20,5):", list(range(0, 20, 5)))
print("range(10,0,-2):", list(range(10, 0, -2)))
print("")

# --- 3. enumerate() ---
print("=== enumerate() ===")
jezici = ["Python", "JavaScript", "C", "Go"]
for indeks, jezik in enumerate(jezici, start=1):
    print(f"  {indeks}. {jezik}")
print("")

# --- 4. zip() — Paralelna iteracija ---
print("=== zip() ===")
imena = ["Vahid", "Enes", "Kemo"]
ocene = [9.2, 8.5, 7.8]
for ime, ocena in zip(imena, ocene):
    print(f"  {ime}: {ocena}")
print("")

# --- 5. BREAK i CONTINUE ---
print("=== break (prekida na 5) ===")
for i in range(10):
    if i == 5:
        break
    print(f"  {i}", end="")
print("")

print("=== continue (preskače neparne) ===")
for i in range(10):
    if i % 2 != 0:
        continue
    print(f"  {i}", end="")
print("\n")

# --- 6. UGNEŽĐENE PETLJE ---
print("=== Tablica množenja (1-5) ===")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print("")

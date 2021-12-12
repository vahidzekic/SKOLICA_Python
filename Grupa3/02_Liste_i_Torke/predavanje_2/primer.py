#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 02_Liste_i_Torke / Predavanje 2
# Tema: Iteracija, list comprehension, ugnežđene liste, kopiranje
# =============================================================================

# --- 1. ITERACIJA SA enumerate() ---
jezici = ["Python", "JavaScript", "C", "HTML/CSS"]
print("=== Iteracija sa enumerate() ===")
for i, jezik in enumerate(jezici):
    print(f"  [{i}] {jezik}")
print("")

# --- 2. LIST COMPREHENSION ---
print("=== List Comprehension ===")

# Kvadrati brojeva od 0 do 9
kvadrati = [x ** 2 for x in range(10)]
print(f"Kvadrati: {kvadrati}")

# Parni brojevi do 20
parni = [x for x in range(21) if x % 2 == 0]
print(f"Parni: {parni}")

# Velika slova iz stringa
tekst = "Zdravo Svete"
velika = [ch for ch in tekst if ch.isupper()]
print(f"Velika slova iz '{tekst}': {velika}")

# Primena funkcije na svaki element
imena = ["vahid", "kemo", "omer"]
kapitalizovana = [ime.capitalize() for ime in imena]
print(f"Kapitalizovana: {kapitalizovana}")
print("")

# --- 3. UGNEŽĐENE LISTE (MATRICE) ---
print("=== Matrice (2D liste) ===")
matrica = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrica:")
for red in matrica:
    print(f"  {red}")
print(f"Element [1][2] = {matrica[1][2]}")  # 6
print("")

# --- 4. KOPIRANJE LISTI ---
print("=== Kopiranje vs Referenca ===")
original = [1, 2, 3, 4, 5]
referenca = original       # Ista memorija!
kopija = original.copy()   # Prava kopija

referenca.append(999)
print(f"Original posle ref.append(999): {original}")  # [1,2,3,4,5,999]!
print(f"Kopija (nepromenjena): {kopija}")              # [1,2,3,4,5]

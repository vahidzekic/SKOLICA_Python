#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 04_Kontrola_Toka_i_Petlje / Predavanje 3
# Tema: WHILE petlja, while-else, sentinel pattern, akumulator
# =============================================================================

# --- 1. OSNOVNA WHILE PETLJA ---
print("=== While petlja: Odbrojavanje ===")
odbrojavanje = 5
while odbrojavanje > 0:
    print(f"  {odbrojavanje}...")
    odbrojavanje -= 1
print("  🚀 Start!")
print("")

# --- 2. WHILE...ELSE ---
print("=== While...Else ===")
i = 0
while i < 3:
    print(f"  Iteracija {i}")
    i += 1
else:
    print("  Petlja je završena normalno (else blok)")
print("")

# --- 3. AKUMULATOR OBRAZAC ---
print("=== Akumulator ===")
brojevi = [4, 7, 2, 9, 1, 5, 8]
suma = 0
najmanji = brojevi[0]
najveci = brojevi[0]

for b in brojevi:
    suma += b
    if b < najmanji:
        najmanji = b
    if b > najveci:
        najveci = b

prosek = suma / len(brojevi)
print(f"  Brojevi: {brojevi}")
print(f"  Suma: {suma}, Prosek: {prosek:.2f}")
print(f"  Min: {najmanji}, Max: {najveci}")
print("")

# --- 4. SENTINEL PETLJA ---
print("=== Sentinel petlja (unesite 'kraj' za izlaz) ===")
lista_unosa = []
while True:
    unos = input("  Unesite reč (ili 'kraj'): ")
    if unos.lower() == 'kraj':
        break
    lista_unosa.append(unos)

print(f"  Uneli ste {len(lista_unosa)} reči: {lista_unosa}")

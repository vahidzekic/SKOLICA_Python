#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 04_Kontrola_Toka_i_Petlje / Predavanje 1
# Tema: if/elif/else, operatori poređenja, logički operatori
# =============================================================================

# --- 1. JEDNOSTAVAN IF ---
godine = 25
if godine >= 18:
    print("Osoba je punoletna.")

# --- 2. IF-ELSE ---
broj = -5
if broj >= 0:
    print(f"{broj} je pozitivan.")
else:
    print(f"{broj} je negativan.")

# --- 3. IF-ELIF-ELSE ---
print("\n=== Sistem ocenjivanja ===")
poeni = 78

if poeni >= 91:
    ocena = 10
elif poeni >= 81:
    ocena = 9
elif poeni >= 71:
    ocena = 8
elif poeni >= 61:
    ocena = 7
elif poeni >= 51:
    ocena = 6
else:
    ocena = 5

print(f"Poeni: {poeni} → Ocena: {ocena}")

# --- 4. LOGIČKI OPERATORI ---
print("\n=== Logički operatori ===")
temperatura = 25
sunce = True

if temperatura > 20 and sunce:
    print("Lep dan za šetnju!")
elif temperatura > 20 or sunce:
    print("Delimično lep dan.")
else:
    print("Ostanite unutra.")

# --- 5. TERNARY OPERATOR ---
print("\n=== Ternary operator ===")
x = 42
parnost = "paran" if x % 2 == 0 else "neparan"
print(f"{x} je {parnost}")

# --- 6. OPERATOR 'in' ---
print("\n=== Operator 'in' ===")
jezici = ["Python", "JavaScript", "C", "Go"]
trazeni = "Python"
if trazeni in jezici:
    print(f"'{trazeni}' je u listi!")

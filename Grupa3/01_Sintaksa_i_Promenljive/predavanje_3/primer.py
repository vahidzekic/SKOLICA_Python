#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 01_Sintaksa_i_Promenljive / Predavanje 3
# Tema: Aritmetičke operacije, input(), operatori dodele
# =============================================================================

# --- 1. ARITMETIČKE OPERACIJE ---
prviBroj = 11
drugiBroj = 7

print("=== Aritmetičke operacije ===")
print(f"{prviBroj} + {drugiBroj} = {prviBroj + drugiBroj}")
print(f"{prviBroj} - {drugiBroj} = {prviBroj - drugiBroj}")
print(f"{prviBroj} * {drugiBroj} = {prviBroj * drugiBroj}")
print(f"{prviBroj} / {drugiBroj} = {prviBroj / drugiBroj:.4f}")
print(f"{prviBroj} // {drugiBroj} = {prviBroj // drugiBroj}")
print(f"{prviBroj} % {drugiBroj} = {prviBroj % drugiBroj}")
print(f"{prviBroj} ** {drugiBroj} = {prviBroj ** drugiBroj}")
print("")

# --- 2. OPERATORI DODELE ---
print("=== Operatori dodele ===")
x = 100
print(f"x = {x}")
x += 10
print(f"x += 10 → {x}")
x -= 5
print(f"x -= 5  → {x}")
x *= 2
print(f"x *= 2  → {x}")
x //= 3
print(f"x //= 3 → {x}")
print("")

# --- 3. REDOSLED OPERACIJA ---
print("=== Redosled operacija (PEMDAS) ===")
rezultat1 = 2 + 3 * 4       # 14, ne 20
rezultat2 = (2 + 3) * 4     # 20
rezultat3 = 2 ** 3 + 1      # 9
print(f"2 + 3 * 4 = {rezultat1}")
print(f"(2 + 3) * 4 = {rezultat2}")
print(f"2 ** 3 + 1 = {rezultat3}")
print("")

# --- 4. KORISNIČKI UNOS ---
print("=== Kalkulator ===")
a = float(input("Unesite prvi broj: "))
b = float(input("Unesite drugi broj: "))

print(f"\nRezultati za {a} i {b}:")
print(f"  Sabiranje: {a + b}")
print(f"  Oduzimanje: {a - b}")
print(f"  Množenje: {a * b}")
if b != 0:
    print(f"  Deljenje: {a / b:.4f}")
else:
    print("  Deljenje: Greška — deljenje nulom!")
